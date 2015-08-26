from flask_app import app, db
from flask import render_template, redirect, session, request, url_for, flash
from user.form import SignupForm, LoginForm
from user.models import User
from user.decorators import login_required

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data,
            password=form.password.data,
        ).limit(1)
        if user.count():
            session['username'] = form.username.data
            flash("User %s logged in" % session['username'])
            app.logger.warning("User logged in (%s)" % request.form.get("username"))            
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
                return redirect('index')
        else:
            error = "Incorrect username and password"
            app.logger.warning("Incorrect username and password (%s, %s)" %
                (request.form.get("username"),request.form.get("password")))
    return render_template('user/login.html', form=form, error=error)
    
@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            form.password.data
        )
        db.session.add(user)
        db.session.flush()
        if user.id:
            db.session.commit()
            flash("New user account created.")
        else:
            db.session.rollback()
            error = "Error creating user"
        return redirect('login')
    return render_template('user/signup.html', form=form)

@app.route('/logout')
def logout():
    # if session['username']:
    session.pop('username')
    flash("User logged out")
    return redirect(url_for('login'))

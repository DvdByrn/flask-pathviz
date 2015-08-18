/*
function initialize_map(json_map) {
    // load everything
    load_builder(json_map, function(builder) {
    });
}


function load_builder(map, callback) {
    // load the Builder
    d3.json(map, function(e, data) {
        if (e) console.warn(e);
        //d3.text("{{ url_for('static', filename='escher/builder-embed-1.2.0.css') }}", function(e, css) {
        d3.text('../static/escher/builder-embed-1.2.0.css', function(e, css) {
            if (e) console.warn(e);
            var options = { menu: 'mb_options',
                            enable_editing: false,
                            fill_screen: false,
                            reaction_styles: ['abs', 'color', 'size', 'text'],
                            never_ask_before_quit: true };
            var b = escher.Builder(data, null, css, d3.select('#map_container'), options);
            callback(b);
        });
    });
}
*/

function initialize_map(json_map) {
    d3.json(json_map, function(e, data) {
        if (e) console.warn(e);
        d3.text('../static/escher/builder-embed-1.2.0.css', function(e, css) {
            if (e) console.warn(e);
            var options = { fill_screen: false,
                            menu: 'mb_options',
                            enable_editing: false,
                            reaction_styles: ['abs', 'color', 'size', 'text'],
                            never_ask_before_quit: true };
            escher.Builder(data, null, css, d3.select('#map_container'), options);
            //var b = escher.Builder(data, null, css, d3.select('#map_container'), options);
            //callback(b);
        });
    });
}
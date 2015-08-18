function initialize_map(json_map) {
    d3.json(json_map, function(e, data) {
        if (e) console.warn(e);
        d3.text('/static/escher/builder-embed-1.2.0.css', function(e, css) {
            if (e) console.warn(e);
            var options = { fill_screen: false,
                            menu: 'mb_options',
                            enable_editing: false,
                            reaction_styles: ['abs', 'color', 'size', 'text'],
                            never_ask_before_quit: true };
            escher.Builder(data, null, css, d3.select('#map_container'), options);
        });
    });
}
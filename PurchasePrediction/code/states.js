function run()
{
    d3.json("stage/states.json", function(error, json) {

        if (error) return console.warn(error);
        
        data = json;

        console.log( data )

        var bubble_map = new Datamap({
            scope: 'usa',
            element: document.getElementById("map"),
                        
            fills: data.fill_keys,
            data: data.states_data,
           
            geographyConfig: {
                    highlightBorderColor: '#ff0000',
                    highlightBorderWidth: 3,
            }
        });

    });

}

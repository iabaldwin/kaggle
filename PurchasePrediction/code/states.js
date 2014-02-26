function run()
{

    d3.json("stage/states.json", function(error, json) {

        if (error) return console.warn(error);
        
        data = json;

        console.log( data.states_data )

        var bubble_map = new Datamap({
            scope: 'usa',
            element: document.getElementById("map"),
            geographyConfig: {
                popupOnHover: false,
                highlightOnHover: false
            },
            highlightBorderColor: '#000000',
            highlightBorderWidth: 3,
            fills: {
                'light': '#667FAF',
                defaultFill: '#888888'
            },
            
            data: data.states_data
                  
        });

    });

}

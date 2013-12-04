var IAB = window.IAB || {};

function flight_locations()
{
    (function () {
        $.ajax({
            'global': false,
            'async': false,
            'url': 'flight_locations.json',
            'dataType': "json",
            'success': function (locations) {
                IAB.flight_locations = locations;
            }
        });

    })(); 
}

function plot_sample_flights()
{
    var flights = IAB.flight_locations.slice( 0, 100);

    IAB.arcs = new Array;
    IAB.bubbles= new Array;

    for ( var i=0; i< flights.length; i++ )
    {
        var matches = IAB.airport_locations.filter(function(val, index, array) {
            return val.designator === flights[i].airport; 
        });

        if ( matches.length != 0 )
        {
            IAB.arcs.push( {
                'origin': { 
                    'latitude': flights[i].lat,
                'longitude': flights[i].long 
                },
                'destination':  {
                    'latitude':matches[0].lat, 
                'longitude':matches[0].long 
                }
            }); 

            IAB.bubbles.push( {latitude:flights[i].lat,
                                    longitude:flights[i].long,
            radius:3
            } );

            var airport = matches[0];
         
            var airport_bubble = {'latitude':airport.lat, 'longitude':airport.long, 'radius':12 };

            if ( !( airport_bubble in IAB.bubbles ))
            {
                IAB.bubbles.push( airport_bubble );
            }
        }
    }

    window.map.arc(IAB.arcs, 
            {
                strokeWidth: 2,
                arcSharpness: 0.1
            });

    window.map.bubbles( IAB.bubbles );
}

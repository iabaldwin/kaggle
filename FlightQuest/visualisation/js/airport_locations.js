var IAB = window.IAB || {};

function airport_locations()
{
    (function () {
        $.ajax({
            'global': false,
            'async': false,
            'url': 'airport_locations.json',
            'dataType': "json",
            'success': function (locations) {
                IAB.airport_locations = locations;
            },
            'failure': function (err) {
                console.err( 'Unable to load data' );
            }
        });

    })(); 
}


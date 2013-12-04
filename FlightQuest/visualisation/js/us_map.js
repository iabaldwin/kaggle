function load_map()
{
    window.map = new Datamap({
        element: document.getElementById("basic"),
        scope: 'usa',
        geographyConfig: {
            popupOnHover: false,
        highlightOnHover: false
          }
    });

}

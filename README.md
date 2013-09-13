dtegeoreference
===============

###approximate georeferencing of the DTE aerial photo collection

This software provides a way to browse, download, and view aerial photographs of the Detroit area from as early as 1949.

original wayne state university source of maps and images: http://www.clas.wayne.edu/photos/ap_index.htm

######"img overlay.py" and the index maps can be used with out knowledge of programming.
it can only be used for counties that have allready been georeferenced (macomb, oakland)

This program is meant to be used with GoogleEarth

output is google earth image overlay .kml and .jpg

georeferencing is only approximate, manual adjustment is necessary.

please note some code is in a rough state and unpolished


##instructions and workflow
Open desired county and year: e.g. "macomb index maps/1961aerialphotos.kml"

It will show an array of place marks in google earth

The names can be used in "img overlay.py", or go to the url in the description (it is recommended that you copy it into a browser rather than click it)

"img overlay.py" is a command line program. all you have to do is enter the county, year, name and choose a folder for the files to be saved.

Then open the .kml file in google earth

Go to "get info"

Manualy adjust the edges so it lines up

Save it to keep your changes


dtegeoreference
===============

This software provides a way to browse, download, and view the DTE Aerial Photo Collection in GoogleEarth.

The DTE Aerial Photo Collection consists of aerial photographs of the Detroit area from 1949 to 1997

original source of maps and images hosted by Wayne State University: http://www.clas.wayne.edu/photos/ap_index.htm

######The index maps and "img overlay.py" can be used with out knowledge of programming.

##instructions and workflow
Open desired county and year: e.g. "macomb index maps/1961aerialphotos.kml"

It will show an array of place marks in google earth

The names can be used in "img overlay.py", or go to the url in the description (it is recommended that you copy it into a browser rather than click it)

"img overlay.py" is a command line program. all you have to do is enter the county, year, and name.

Then open the .kml file in google earth

Go to "get info"

Manualy adjust the edges so it lines up

Save it to keep your changes

##other things to know about this software
automatic georeferencing is only approximate, manual adjustment is necessary.

It does not orthorectify the images. this means distortion will appear on hills and the image will not line up perfectly with modern imagery

please note some code is in a rough state and unpolished

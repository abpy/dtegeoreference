dtegeoreference
===============

<!---This software provides a way to browse, download, and view the DTE Aerial Photo Collection in GoogleEarth.-->

A set of Google Earth placemarks for the DTE Aerial Photo Collection. And a script to make an approximate image overlay.

The DTE Aerial Photo Collection consists of aerial photographs of the Detroit area from 1949 to 1997

original source of maps and images hosted by Wayne State University: http://claslinux.clas.wayne.edu/photos/ap_index.htm

##instructions and usage
Open desired county and year: e.g. "macomb index maps/1961aerialphotos.kml"

The place mark names names can be used in "img overlay.py", or go to the url in the description (it is recommended that you copy it into a browser rather than click it)

To make an approximate image overlay for Google Earth:

run "img overlay.py"

enter the county, year, and name.

it will write a kml file and a jpeg image for the image overlay

##other things to know about this software
automatic georeferencing is only approximate, manual adjustment is necessary.

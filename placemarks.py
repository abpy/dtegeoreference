#import urllib2

county = "oakland"
year = "1967"

maindir = "http://www.clas.wayne.edu/photos/part1/" + county + "/" + year +"/"
#pdf = urllib2.urlopen(maindir + "macomb" + year[2:4] + "Index.pdf")

countydir = county + " index maps/"

pdf = open(countydir + county + year[2:4] + "Index.pdf")
data = pdf.read()
pdf.close()

#create dictionary of pdf objects
objects = data.split("endobj")
objects_dict = {}
for st in objects:
    st = st.split("\r")
    name = st[1].split(" ")[0]
    obj_dict = {}
    for l in st:
        l = l.split(" ")
        iname = l[0]
        obj_dict[iname] = l[1:]
    
    objects_dict[name] = obj_dict

#sfor i in objects_dict["31"]: print i, objects_dict["31"][i]

#get stuff from objects
images = []
for item in objects_dict:
    obj = objects_dict[item]
    try:
        coord = obj["/Rect"]
        nextobj = obj["/A"][0]
        urlobj = objects_dict[nextobj]["/F"][0]
        url_ = objects_dict[urlobj]["/F"][0]
        coords = (float(coord[1]), float(coord[2]))
        url = maindir + url_[1:-1]
        imname = url_[1:-5]
        image = [coords, url, imname]
        images.append(image)
    except KeyError:
        pass
    try:
        docsize = obj["/CropBox"]
        docsize = (float(docsize[3]), float(docsize[4]))
    except KeyError:
        pass

#geographic extent of pdf
##if year == "1949":
##    north = 42.922804
##    south = 42.415587
##    east = -82.647680
##    west = -83.149261
##elif year == "1952":
##    north = 42.926226
##    south = 42.412952
##    east = -82.669406
##    west = -83.157601
##elif year == "1956":
##    north = 42.945220
##    south = 42.406166
##    east = -82.672217
##    west = -83.152436
##elif year == "1961":
##    north = 42.928785
##    south = 42.381478
##    east = -82.671840
##    west = -83.156916
##elif year == "1967":
##    north = 42.943869
##    south = 42.420650
##    east = -82.666344
##    west = -83.157358
if year == "1949":
    north = 42.918480
    south = 42.403073
    east = -82.842176
    west = -83.739028
elif year == "1952":
    north = 42.990343
    south = 42.408732
    east = -83.067526
    west = -83.718846
elif year == "1956":
    north = 42.938540
    south = 42.427244
    east = -82.833311
    west = -83.716104
elif year == "1967":
    north = 43.044730
    south = 42.383892
    east = -83.068028
    west = -83.730652

#get scales and convert pdf units to degrees
lat_width = abs(west - east)
lon_height = abs(north - south)

xscale = lat_width / docsize[0]
yscale = lon_height / docsize[1]

for i, image in enumerate(images):
    x = image[0][0]
    y = image[0][1]
    lon = east - ((docsize[0] - x) * xscale) - .001
    lat = south + (y * yscale) + .004
    images[i][0] = (lat, lon)

imageslist = open(countydir + year + county + ".txt", "w")
images_list_text = ""
for im in images:
    images_list_text += str(im[2]) + "," + str(im[0][0]) + "," + str(im[0][1]) + "\n"

imageslist.write(images_list_text)
imageslist.close()

#write kml
kmlfile = open(countydir + year + county + " aerial photos.kml", "w")
head = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
"""
folder = "\t<name>" + year + "aerial photos.kml</name>\n\
\t\t<Folder>\n\
\t\t\t<name>" + year + "aerial photos</name>\n"
folder += "\t\t\t<LookAt>\n"
folder += "\t\t\t\t<longitude>%s</longitude>\n" % ((east - (east - west) / 2))
folder += "\t\t\t\t<latitude>%s</latitude>\n" % ((south + (north - south) / 2))
folder += "\t\t\t\t<altitude>0</altitude>\n"
folder += "\t\t\t\t<heading>0</heading>\n"
folder += "\t\t\t\t<tilt>0</tilt>\n"
folder += "\t\t\t\t<range>65000</range>\n"
folder += "\t\t\t\t<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>\n"
folder += "\t\t\t</LookAt>\n"

kmlfile.write(head)
kmlfile.write(folder)
footer = """\t\t</Folder>
</Document>
</kml>"""

for im in images:
    lat = im[0][0]
    lon = im[0][1]
    url = im[1]
    name = im[2]
    placemark = ""
    placemark += "\t\t\t<Placemark>\n"
    placemark += "\t\t\t\t<name>%s</name>\n" % (name)
    placemark += "\t\t\t\t<description><![CDATA[<a href=\"%s\">%s</a>]]></description>\n" % (url, url)
    placemark += "\t\t\t\t<LookAt>\n"
    placemark += "\t\t\t\t\t<longitude>%s</longitude>\n" % (lon)
    placemark += "\t\t\t\t\t<latitude>%s</latitude>\n" % (lat)
    placemark += "\t\t\t\t\t<altitude>0</altitude>\n"
    placemark += "\t\t\t\t\t<heading>0</heading>\n"
    placemark += "\t\t\t\t\t<tilt>0</tilt>\n"
    placemark += "\t\t\t\t\t<range>4000</range>\n"
    placemark += "\t\t\t\t\t<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>\n"
    placemark += "\t\t\t\t</LookAt>\n"
    placemark += "\t\t\t\t<styleUrl>#m_ylw-pushpin</styleUrl>\n"
    placemark += "\t\t\t\t<Point>\n"
    placemark += "\t\t\t\t\t<coordinates>%s,%s,0</coordinates>\n" % (lon, lat)
    placemark += "\t\t\t\t</Point>\n"
    placemark += "\t\t\t</Placemark>\n"

    kmlfile.write(placemark)

kmlfile.write(footer)
kmlfile.close()




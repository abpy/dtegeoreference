import urllib2
import time
import sys

def download_pdf_to_jpg(county, year, name):
    if county == "wayne":
        part = "part2/"
    else:
        part = "part1/"
    pdf = urllib2.urlopen("http://claslinux.clas.wayne.edu/photos/" + part + county + "/" + year + "/" + name + ".pdf")
    print "downloading", name, "..."
    t1 = time.time()
    pdfimg = pdf.read()
    pdf.close()

    if pdfimg[2:16] == "<!DOCTYPE html":
        print "This image is not available"
        sys.exit()

    streams = pdfimg.split("stream")

    for s in streams:
        if len(s) > 100000:
            jpeg = s[2:-5]
        else:pass

    jpegfile = open("photographs/" + name + ".jpg", "wb")
    jpegfile.write(jpeg)
    jpegfile.close()

    t2 = time.time()
    print t2 - t1
    print "done"

def image_overlay_kml(county, year, name):
    countydir = county + " index maps/"

    #get location
    imgfile = open(countydir + year + county + ".txt", "r")
    imglist = imgfile.readlines()
    imgfile.close()

    imgdict = {}
    for i in imglist:
        i = i[:-1].split(",")
        imgdict[i[0]] = (float(i[1]), float(i[2]))

    location = imgdict[name]

    # dimensions in degrees of a photo
    height = 0.027895
    width = 0.039518

    #geographic bounds
    north = location[0] + (height / 2)
    south = location[0] - (height / 2)
    east = location[1] + (width / 2)
    west = location[1] - (width / 2)

    #image overlay
    kmlf = open("overlay_template.txt", "r")
    template = kmlf.read()
    kmlf.close()

    overlaykml = template % (name + "overlay", location[1], location[0], "../photographs/"+ name + ".jpg", north, south, east, west)

    file = open("kml overlays/" + name + "overlay.kml", "w")
    file.write(overlaykml)
    file.close()

county = raw_input("county: ")
year = raw_input("year: ")
name = raw_input("name: ")

download_pdf_to_jpg(county, year, name)
image_overlay_kml(county, year, name)

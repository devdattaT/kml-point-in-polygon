from fastkml import kml
from shapely.geometry import Point, LineString, Polygon





def readKMLFile(path):
    k = None
    with open(path, 'rb') as kmlFile:
        doc=kmlFile.read()
        k=kml.KML()
        k.from_string(doc)
    return k

#Point Data in Lat-Long
pune = [18.543483503618656, 73.80872027889882]
bengaluru = [12.995445134539802, 77.53686034222525]

# We will make Point data from the arrays
pune_pt=Point(pune[1], pune[0])
blr_pt =Point(bengaluru[1], bengaluru[0])

KMLdata = readKMLFile('doc.kml')

features = list(KMLdata.features())
#Get the Placemark
placemark = features[0].features()

for p in placemark:
    #get the geometry
    geom = p.geometry
    pune_in_poly = geom.contains(pune_pt)
    print("Is Pune in this Polygon? {0}".format(pune_in_poly))

    blr_in_poly = geom.contains(blr_pt)
    print("Is Bengaluru in this Polygon? {0}".format(blr_in_poly))

    

    
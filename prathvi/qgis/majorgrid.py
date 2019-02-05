#get from kml
from fastkml import kml
doc = file("mykml.kml").read()
#with open('C:\\Users\\Prathvi\\Desktop\prj\\codes\\qgis\\mykml.kml') as myfile:
	#doc=myfile.read()
k = kml.KML()
k.from_string(doc)
features = list(k.features())
f2 = list(features[0].features())
f2[0].name
val=f2[0]._geometry.geometry._coordinates
#--------------------------
pos=[80,20];
r=5;
import math
from qgis.core import *
layer = iface.addVectorLayer('I:\\TM_WORLD_BORDERS-0.3\\TM_WORLD_BORDERS-0.3.shp','test','ogr')
features=layer.featureCount()
vpr = layer.dataProvider()

val=r/math.sqrt(2);

poly= QgsGeometry.fromPolygonXY([[QgsPointXY(pos[0]+val,pos[1]+val),QgsPointXY(pos[0]-val,pos[1]+val), QgsPointXY(pos[0]-val,pos[1]-val), QgsPointXY(pos[0]+val,pos[1]-val)]])

f=QgsFeature();
f.setGeometry(poly);
f.setAttributes([features])
vpr.addFeatures([f])
layer.updateExtents()
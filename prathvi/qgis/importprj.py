from qgis.core import *

qgs = QgsApplication([], False)
qgs.initQgis()
print(project.fileName);
project.read('C:\\Users\\Prathvi\\Downloads\\Natural_Earth_quick_start\packages\\Natural_Earth_quick_start\\Natural_Earth_quick_start_for_QGIS.qgs')

# to load the layer
layer= QgsVectorLayer('I:\\Mango Tutorial - Filtering a Dataset - US Counties\\US Counties\\US Counties.shp','test','ogr');


# to display the layer

layer = iface.addVectorLayer('I:\\Mango Tutorial - Filtering a Dataset - US Counties\\US Counties\\US Counties.shp','test','ogr')

#count number of features
features=layer.featureCount()
vpr = layer.dataProvider()

#make a polygon here a triangle
poly= QgsGeometry.fromPolygonXY([[QgsPointXY(50,50),QgsPointXY(100,150), QgsPointXY(100,50)]])

#ready feature 
f=QgsFeature();

#add the geometry
f.setGeometry(poly);

#set the feature atrib
f.setAttributes([features])

#add feature to the map
vpr.addFeatures([f])

#update layers
layer.updateExtents()

#EPSG:3857



#---------------------in kml

#obj.__dict__ shows the attributes of an object

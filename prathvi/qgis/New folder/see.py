import sys
sys.path.append( 'c:\\python27\\lib\\site-packages');
import time

start=time.time();

from pykml import parser
#from qgis.core import *
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84 
import math
from copy import deepcopy
import simplekml
kml = simplekml.Kml()
#-----------------------assumptions-----------------------

dronesnr=20;
battery=3300;
n=2;
dist_of_location=1000;#in meters



#--------------------------------------------------------------
#------------------------declaration for model-----------------

numcenter=0;
speed=6;

#--------------------------------------------------------------



file = parser.fromstring(open('C:\\Users\\Prathvi\\Desktop\prj\\repo\\prathvi\\qgis\\85.kml', 'r').read())

#file.Document.Placemark.Point.coordinates ==> to check once if want..

num, cor = 2,4;
cords = [[0.0 for x in range(num)] for y in range(cor)] # create empty 4*3 matrix

for x in range(cor):
	for y in range(num):
		cords[x][y]=float(str(file.Document.Placemark.Point[x].coordinates).split(',')[y]);

cordsmap=deepcopy(cords)

for i in range(cor):
	cordsmap[i].reverse()



# layer = iface.addVectorLayer('I:\\TM_WORLD_BORDERS-0.3\\TM_WORLD_BORDERS-0.3.shp','test','ogr')
# features=layer.featureCount()
# vpr = layer.dataProvider()
# poly= QgsGeometry.fromPolygonXY([[QgsPointXY(cordsmap[0][0],cordsmap[0][1]),QgsPointXY(cordsmap[1][0],cordsmap[1][1]), QgsPointXY(cordsmap[2][0],cordsmap[2][1]), QgsPointXY(cordsmap[3][0],cordsmap[3][1])]])
# f=QgsFeature();
# f.setGeometry(poly);
# f.setAttributes([features])
# vpr.addFeatures([f])

#-------------to find total area-------------------------------
p = geod.Polygon()
for pnt in cords:
	p.AddPoint(pnt[0], pnt[1])

num, perim, area = p.Compute()
area=abs(area);


#--------------------------------------------------------------
#-----------------------model----------------------------------

capacity=battery/1000*0.9;
maxtime=(capacity/8)*60*60;
maxdist=(maxtime*speed)-2*(dist_of_location);
distdrone=maxdist*dronesnr;
maxarea=n*distdrone;

numcenter=math.floor(area/maxarea)
presarea=area-numcenter*maxarea;
eacharea=presarea/dronesnr
numcenter=3
print("_____________________________________________")
print("each drone have to cover area of ",eacharea)
print("number of extra centers required is",numcenter);
print("_____________________________________________")

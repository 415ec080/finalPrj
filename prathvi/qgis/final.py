import sys
sys.path.append( 'c:\\python27\\lib\\site-packages');

from pykml import parser
from qgis.core import *
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84 
import math
from copy import deepcopy
import simplekml
kml = simplekml.Kml()
#-----------------------assumptions-----------------------

dronesnr=12;
battery=3300;
n=2;
dist_of_location=1000;#in meters


#---------------definations--------------------------------------
def exprt(toexp):
	kml = simplekml.Kml()
	for x in range(len(toexp)):
		kml.newpolygon(name=str(x), outerboundaryis=toexp[x])
		kml.save("C:\\Users\\Prathvi\\Desktop\\prj\\codes\\qgis\\testfile.kml")




def findTotalArea(pts):
	p = geod.Polygon()
	for pnt in pts:
		p.AddPoint(pnt[0], pnt[1])
	num, perim, area = p.Compute()
	area=abs(area);
	return area

def rectify(point):
	y=len(point)
	points=[]
	for i in range(1,y,2):
		points.append(point[i])
	points.append(point[0])
	for i in range(y-1,1,-2):
		points.append(point[i])
	return points


def findarea(point):
	y=len(point)
	points=[]
	for i in range(1,y,2):
		points.append(point[i])
	points.append(point[0])
	for i in range(y-1,1,-2):
		points.append(point[i])
	p = geod.Polygon()
	for pnt in points:
		p.AddPoint(pnt[0], pnt[1])
	num, perim, area = p.Compute()
	area=abs(area);
	return area
#---------------------------------------------------------


#--------------------------------------------------------------
#------------------------declaration for model-----------------

numcenter=0;
speed=6;

#--------------------------------------------------------------



file = parser.fromstring(open('C:\\Users\\Prathvi\\Desktop\prj\\codes\\qgis\\85.kml', 'r').read())

#file.Document.Placemark.Point.coordinates ==> to check once if want..

num, cor = 2,4;
cords = [[0.0 for x in range(num)] for y in range(cor)] # create empty 4*3 matrix

for x in range(cor):
	for y in range(num):
		cords[x][y]=float(str(file.Document.Placemark.Point[x].coordinates).split(',')[y]);

cordsmap=deepcopy(cords)

for i in range(cor):
	cordsmap[i].reverse()



layer = iface.addVectorLayer('I:\\TM_WORLD_BORDERS-0.3\\TM_WORLD_BORDERS-0.3.shp','test','ogr')
features=layer.featureCount()
vpr = layer.dataProvider()
poly= QgsGeometry.fromPolygonXY([[QgsPointXY(cordsmap[0][0],cordsmap[0][1]),QgsPointXY(cordsmap[1][0],cordsmap[1][1]), QgsPointXY(cordsmap[2][0],cordsmap[2][1]), QgsPointXY(cordsmap[3][0],cordsmap[3][1])]])
f=QgsFeature();
f.setGeometry(poly);
f.setAttributes([features])
vpr.addFeatures([f])

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
print("_____________________________________________")
print("each drone have to cover area of ",eacharea)
print("number of extra centers required is",numcenter);
print("_____________________________________________")

# to make smaller sized total area
num, cor = 2,4;
pressize=math.sqrt(presarea)
g = geod.Direct(cords[0][0],cords[0][1], 90, pressize)
g['lat2'],g['lon2']=cords[0][0],cords[0][1];
newcords = [[0.0 for x in range(num)] for y in range(cor)]
for x in range(4):
	g = geod.Direct(g['lat2'],g['lon2'],(x+((-1)**x))*90 , pressize)	
	newcords[x][0],newcords[x][1]=g['lat2'],g['lon2']


#--------------------------------------------------------------
#--------------------side--------------------------------------
cos=newcords;
num=dronesnr;
reqarea=eacharea;
toexp=[]


for x in range(0,(num-1)):
	x=len(cos)-1
	points=[]
	points.append(cos[x])
	points.append(cos[(x-1)%(x+1)])
	points.append(cos[(x+1)%(x+1)])
	y=len(points)-1
	max2=points[y]
	max1=points[y-1]	
	min1=points[y-2]
	min2=points[y-2]
	area=findarea(points)
	while ((area-reqarea)<-0.001 or (area-reqarea)>0.001):
		if area<reqarea:
			min1=points[1]
			min2=points[2]
			if min1==max1:
				points.insert(1,cos[(x-2)%(x+1)])
				max1=points[1]
			if min2==max2:
				points.insert(2,cos[(x+2)%(x+1)])
				max2=points[2]
			points[2]=max2
			points[1]=max1
		else:
			max1=points[1]
			max2=points[2]
			points[1]=[float((points[1][0]+min1[0])*0.5),float((points[1][1]+min1[1])*0.5)]
			points[2]=[float((points[2][0]+min2[0])*0.5),float((points[2][1]+min2[1])*0.5)]
		area=findarea(points)
		print(area)
	print("--------------------------------------------------")
	print(points)
	#export(points)
	toexp.append(rectify(points));
	y=len(points)
	for x in range(0,y):
		try:
			cos.remove(points[x])
			print("removed")
		except:
			cos.append(points[x])
			print("exception")
	print("--------------------------------------------------")

toexp.append(cos);
#--------------------------------------------------------------
#final cos is in points[]
exprt(toexp)

points=toexp;

#--------------------------------------------------------------

#----------------drawing in map--------------------------------
# for x in range(dronesnr):
# 	poly=QgsGeometry.fromPolygonXY([[QgsPointXY(points[x][0][1],points[x][0][0]),QgsPointXY(points[x][1][1],points[x][1][0]),QgsPointXY(points[x][2][1],points[x][2][0]),QgsPointXY(points[x][3][1],points[x][3][0])]])
# 	f=QgsFeature();
# 	f.setGeometry(poly);
# 	f.setAttributes([features])
# 	vpr.addFeatures([f])

print("===============>done<====================")

#--------------------------------------------------------------

# 75.9,16.1	--- 75.9,16.4 ----- 76.2,16.4 ---- 76.2,16.1
# 16.1,75.9 --- 16.4,75.9 ----- 16.4,76.2 ---- 16.1,76.2 .9

#[[(16.010876568366573, 75.09), (16.01, 75.09), (16.009999998087924, 75.09090629591385), (16.010876566454385, 75.09090629986781)], [(16.010876566454385, 75.09090629986781), (16.009999998087924, 75.09090629591385), (16.009999996175846, 75.09181259182769), (16.0108765645422, 75.09181259973562)], [(16.0108765645422, 75.09181259973562), (16.009999996175846, 75.09181259182769), (16.00999999426377, 75.09271888774151), (16.010876562630013, 75.09271889960341)], [(16.010876562630013, 75.09271889960341), (16.00999999426377, 75.09271888774151), (16.009999992351688, 75.09362518365533), (16.010876560717826, 75.0936251994712)], [(16.011753129013393, 75.09), (16.010876560718255, 75.09), (16.01087655880607, 75.09090629986778), (16.011753127101095, 75.090906303822)], [(16.011753127101095, 75.090906303822), (16.01087655880607, 75.09090629986778), (16.010876556893887, 75.09181259973555), (16.0117531251888, 75.09181260764397)], [(16.0117531251888, 75.09181260764397), (16.010876556893887, 75.09181259973555), (16.0108765549817, 75.09271889960331), (16.011753123276502, 75.09271891146595)], [(16.011753123276502, 75.09271891146595), (16.0108765549817, 75.09271889960331), (16.010876553069515, 75.09362519947106), (16.011753121364208, 75.09362521528791)], [(16.012629689588334, 75.09), (16.011753121364645, 75.09), (16.01175311945235, 75.09090630382197), (16.01262968767593, 75.09090630777642)], [(16.01262968767593, 75.09090630777642), (16.01175311945235, 75.09090630382197), (16.011753117540053, 75.09181260764392), (16.01262968576352, 75.09181261555283)], [(16.01262968576352, 75.09181261555283), (16.011753117540053, 75.09181260764392), (16.011753115627755, 75.09271891146585), (16.01262968385111, 75.09271892332923)], [(16.01262968385111, 75.09271892332923), (16.011753115627755, 75.09271891146585), (16.011753113715457, 75.09362521528779), (16.012629681938705, 75.09362523110562)], [[0.0], [0.0], [0.0], [0.0]], [[0.0], [0.0], [0.0], [0.0]], [[0.0], [0.0], [0.0], [0.0]], [[0.0], [0.0], [0.0], [0.0]]]
#poly=QgsGeometry.fromPolygonXY([[QgsPointXY(points[0][0][1],points[0][0][0]),QgsPointXY(points[0][1][1],points[0][1][0]),QgsPointXY(points[0][2][1],points[0][2][0]),QgsPointXY(points[0][3][1],points[0][3][0])]])

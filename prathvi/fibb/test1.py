from pykml import parser
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84 
import math
import simplekml
num, cor = 2,4;
numcenter=0;
from copy import deepcopy

#---assumptions
dronesnr=10;
battery=3300;
n=2;
dist_of_location=1000;#in meters
speed=6;

def import_cord():
    file = parser.fromstring(open('C:\\Users\\Prathvi\\Desktop\prj\\repo\\prathvi\\qgis\\85.kml', 'r').read())
    cords = [[0.0 for x in range(num)] for y in range(cor)] # create empty 4*3 matrix
    for x in range(cor):
	    for y in range(num):
		    cords[x][y]=float(str(file.Document.Placemark.Point[x].coordinates).split(',')[y]);
    return cords

def getcenter(cord):
    center=[(cord[0][0]+cord[2][0])/2,(cord[0][1]+cord[2][1])/2]
    return center


def getminarea(cord):
    p = geod.Polygon()
    for pnt in cord:
        p.AddPoint(pnt[0], pnt[1])
    print("pts added")   
    num, perim, area = p.Compute()
    area=abs(area);
    print("area of given cords:",area)
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
    print("max area is ",maxarea)
    print("presarea is ",presarea)
    print(" area is ",area)
    print("number of extra centers required is",numcenter);
    print("_____________________________________________")
    return presarea

def getxval(maxarea,n):
    n1 = 0
    n2 = 1
    count = 0
    total=0
    while count < n:
        nth = n1 + n2
        n1 = n2
        count =count+ (n1*n1)
        n2 = nth
    print(count)
    xval=math.sqrt(maxarea/(count))
    return xval
    # area of last square must be equal to max area for the drone to complete it. 
    # area of last square is equal to m^2 times the area of initial square where m is fibb number
    # hence m^2.x.y=maxeacharea; x=y;=> m^2.x^2=maxeacharea; x= as above
    
        

def getshiftedcord(g):
    shcord=[g['lat2'],g['lon2']]
    return shcord

def calcbBox(x,center,count,m):
    diag=m*x*math.sqrt(2)
    if count%4==0:
        g = geod.Direct(center[0], center[1], 45, diag)
        newcord=getshiftedcord(g)
    if count%4==1:
        g = geod.Direct(center[0], center[1], 135, diag)
        newcord=getshiftedcord(g)
    if count%4==2:
        g = geod.Direct(center[0], center[1], 225, diag)
        newcord=getshiftedcord(g)
    if count%4==3:
        g = geod.Direct(center[0], center[1], 315, diag)
        newcord=getshiftedcord(g)
    bBox=[center,newcord]
    return bBox

def exp(indcords,file):
    kml = simplekml.Kml()
    for x in range(dronesnr):
        print(x)
        pol = kml.newpolygon(name=str(x))
        pol.outerboundaryis = indcords[x]
        kml.save(file)

def getcords(x,center,n):
    finalcords=[]
    count=0
    n1=0
    n2=1
    bBox=[[0,0],[0,0]]
    bBox[1]=center
    while count<n:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        bBox=calcbBox(x,bBox[1],count,n1)
        finalcords.append(bBox)
        print(bBox)
        count += 1
    return finalcords

def exp(indcords,file):
    kml = simplekml.Kml()
    for x in range(dronesnr):
        print(x)
        pol = kml.newpolygon(name=str(x))
        pol.outerboundaryis = indcords[x]
        kml.save(file)


def getfullcords(cords):
    i=0
    finalcords=[]
    for x in cords:
        finalcords.append([x[0],[x[0][0],x[1][1]],x[1],[x[1][0],x[0][1]]])
    return finalcords

cord=import_cord()
center=getcenter(cord)
maxeacharea=getminarea(cord)
x=getxval(maxeacharea,dronesnr)
cords=getcords(x,center,dronesnr)
indcords=getfullcords(cords)
mapcords=deepcopy(indcords)

for i in range(len(mapcords)):
    for j in range(len(mapcords[i])):
        mapcords[i][j]=mapcords[i][j][::-1]

exp(mapcords,"fibb_map_10.kml")
exp(indcords,"fibb_qgis_10.kml")



    
#"Polygon.kml"
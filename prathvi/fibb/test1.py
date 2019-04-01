from pykml import parser
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84 
import math

num, cor = 2,4;
numcenter=0;


#---assumptions
dronesnr=12;
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
    num, perim, area = p.Compute()
    area=abs(area);
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
    print("each drone have to cover area of ",maxarea)
    print("number of extra centers required is",numcenter);
    print("_____________________________________________")
    return eacharea

def getxval(maxarea,n):
    n1 = 0
    n2 = 1
    count = 0
    total=0
    while count < n:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    
    xval=math.sqrt(maxarea/(n1*n1))
    return xval
        

def calcbBox(x,center,count,m):
    if count%4==0:
        diag=m*x*x*math.sqrt(2)
        g = geod.Direct(center[0], center[1], 45, diag)
    if count%4==1:

    if count%4==2:
        
    if count%4==3:

    bBox=[x,corner]
    return bBox

def getcords(x,center,n):
    count=0
    n1=0
    n2=1
    while count<n:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        bBox=calcbBox(x,center,count,n1)


    return finalcords

cord=import_cord()
center=getcenter(cord)
maxeacharea=getminarea(cord)
x=getxval(maxeacharea,dronesnr)
cords=getcords(x,center,dronesnr)

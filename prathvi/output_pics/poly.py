import sys
sys.path.append( 'C:\\Users\\Prathvi\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages');

from pykml import parser

import simplekml
num, cor = 2,4;
numcenter=0;
from copy import deepcopy


def exp(indcords,file):
    kml = simplekml.Kml()
    for x in range(len(indcords)):
        print(x)
        pol = kml.newpolygon(name=str(x))
        pol.outerboundaryis = indcords[x]
        kml.save(file)



def import_cord(file_name):
    file = parser.fromstring(open(file_name, 'r').read())
    cords = [[0.0 for x in range(num)] for y in range(cor)] # create empty 4*3 matrix
    for x in range(cor):
	    for y in range(num):
		    cords[x][y]=float(str(file.Document.Placemark.Point[x].coordinates).split(',')[y]);
    return cords


cords=import_cord('C:\\Users\\Prathvi\\Desktop\\prj\\repo\\prathvi\\output_pics\\85.kml')
cords=[cords]
mapcords=deepcopy(cords)

for i in range(len(mapcords)):
    for j in range(len(mapcords[i])):
        mapcords[i][j]=mapcords[i][j][::-1]


exp(mapcords, 'C:\\Users\\Prathvi\\Desktop\\prj\\repo\\prathvi\\output_pics\\85_poly.kml')
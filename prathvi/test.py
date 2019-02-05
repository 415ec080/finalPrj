import sys
sys.path.append( 'c:\\python27\\lib\\site-packages');
from geographiclib.geodesic import Geodesic
geod = Geodesic.WGS84 
import simplekml
kml = simplekml.Kml()

#from qgis.core import *


#---------------definations--------------------------------------
def exprt(toexp):
	kml = simplekml.Kml()
	for x in range(len(toexp)):
		kml.newpolygon(name=str(x), outerboundaryis=toexp[x])
		kml.save("C:\\Users\\Prathvi\\Desktop\\prj\\codes")




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

#-----------------declaration and assignments--------------
cos=[[16.011409914182767, 75.08999998977038],[16.01140991913003, 75.09145773964711],[16.00999999505319, 75.09145773964711],[16.009999990105925, 75.08999998977038]] #input co-ordinates
num=12 #num of drones
reqarea=findTotalArea(cos)/num;
toexp=[]
#---------------------------------------------------------
#----------------calculations------------------------------
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
	while ((area-reqarea)<-0.01 or (area-reqarea)>0.01):
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

exprt(toexp)






#----------------area<reqarea and max and min values will be same--------------------
# if min1==max1:
# 	points.insert(1,cos[(x-2)%(x+1)])
# 	max1=points[1]


# if min2==max2:
#     points.insert(2,cos[(x+2)%(x+1)])
#     max2=points[2]
#     #--------------------------------------------------


# cos.remove(cos[x])
# cos.append(points[1])
# cos.append(points[2])
# #say reqarea=6000 and got 5000
# #-----------area<reqarea-----------
# min1=points[1]
# min2=points[2]
# #add if here
# points[2]=max2
# points[1]=max1
#  #---------------------------------

# #---------------------area>reqarea
# max1=points[1]
# max2=points[2]

# points[1]=[float((points[1][0]+min1[0])*0.5),float((points[1][1]+min1[1])*0.5)]
# points[2]=[float((points[2][0]+min2[0])*0.5),float((points[2][1]+min2[1])*0.5)]

# #----------------------------------------------------------------------------

# area=findarea(points)
# print(area)
# print(reqarea)
# points

# min1
# min2
# max1
# max2

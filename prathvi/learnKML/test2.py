import sys

sys.path.append('C:\users/prathvi/anaconda3/lib/site-packages')
from simplekml import Kml,Color;


kml=Kml(open=1);

multipnt = kml.newmultigeometry(name="MultiPoint")


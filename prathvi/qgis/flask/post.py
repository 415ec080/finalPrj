import requests
#from pykml import parser

posturl='http://localhost:8081/login'
s = open('C:\\Users\\Prathvi\\Desktop\prj\\codes\\qgis\\85.kml', 'r').read()
vals={"file":s}
print(vals);
values={'upload_file' : 'file.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
r=requests.post(url=posturl,data=vals);
print(r.text);
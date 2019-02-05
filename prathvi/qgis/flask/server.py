from flask import Flask, redirect, url_for, request
app = Flask(__name__)

data=""

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    data = request.form#['nm']
    print(data["file"])
    text_file = open("./Output.kml", "w")
    text_file.write("%s" % data["file"])
    return "hai"

if __name__ == '__main__':
    app.debug=True
    app.run(port=8081)




    #http://demo0249907.mockable.io/test5
var http=require('http')
var fs=require('fs')

http.createServer(function (request,response) {
  response.writeHead(200)
  response.write("hi")
  response.end()
}).listen(8081)
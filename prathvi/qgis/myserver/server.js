var http=require('http');

http.createServer(function(req,res){
    res.writeHead(200);
    res.end("hai");
    console.log("connected")
}).listen(8081);
console.log("8081");
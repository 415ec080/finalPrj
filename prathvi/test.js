var express=require('express');
var request=require('request');
app=express();
app.listen(8081,function(){
    console.log("at 8081");
});

app.get('/',function(req,res){
	res.writeHead(200,{'Content-Type':'text/HTML'});
request.get('http://google.com',function(err,data){
res.write(toString(data));
//console.log(typeof());
res.end();
});

});
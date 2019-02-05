var net=require('net')
var socket = new net.Socket();
socket.connect(8081, "localhost", function () {
    console.log("Client: Connected to server");
    socket.write("GET /rest/whoami HTTP/1.1\r\n\r\n");
     console.log('SOCKET GET REQUEST SEND');
     socket.on('data',function(data){
         var js= JSON.stringify(String(data));
         console.log(js);
     });
});
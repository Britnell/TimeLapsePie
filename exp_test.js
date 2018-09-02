const express = require('express');

// 		** 		Camera

var RaspiCam = require("raspicam");
//var RaspiCam = require("../lib/raspicam");

	//var camera = new RaspiCam({ opts });
var camera = new RaspiCam({
mode: "photo",
output: "./public/cam.jpg",
encoding: "jpg",
timeout: 0 // take the picture immediately
});

camera.on("start", function( err, timestamp ){
console.log("photo started at " + timestamp );
});

camera.on("read", function( err, timestamp, filename ){
console.log("photo image captured with filename: " + filename );
});

camera.on("exit", function( timestamp ){
console.log("photo child process has exited at " + timestamp );
});

camera.start();

// 		** 		Express

var app = express();

app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.send('Hello Express test and excess mess')
});

app.listen(process.env.PORT || 3000)


/*
 *	Cam started on one page
 *	  static img then showed on another...
 */
 
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
camera.stop();		//
console.log("Now stop");
});

camera.on("exit", function( timestamp ){
console.log("photo child process has exited at " + timestamp );
});

// 		** 		Express

var app = express();

app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.send('Hello Express test and excess mess')
});

app.get('/photo', (req, res) => {
    camera.start();
    res.send('Hello Express test and excess mess <br> starting cam'
    	+'<br><a href="/camtest.html">SHow ITTT </a>')
});

app.get('/show', (req, res) => {
	res.send('<img src="/cam.jpg" width="800" height="600">');
});

app.listen(process.env.PORT || 3000)


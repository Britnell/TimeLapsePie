/*
    # # # # ------------   
*/



	// * Setup
	const express = require('express'); // running immediately
	const path = require('path');

    const app = require('express')(); // running immediately
  const server = require('http').Server(app);
const io = require('socket.io')(server);
const port = 3000;

server.listen(port, () =>  {
  console.log(`Server is runnign port ${port} `);
} );



	// * Express

app.get('/', (req,res) => {
  res.sendFile(__dirname +'/public/index.html');
});

app.use(express.static('public'));

//app.use('/public', express.static(path.join(__dirname+'/public') ));

// app.get('/room1', (req,res) => {
//   res.sendFile(__dirname +'/public/room1.html');
// });

// app.get('/paper', (req,res) => {
//   res.sendFile(__dirname +'/public/paper.html');
// });

	// *  Socket

	// IO refers to server side obj / event
const imgSpace = io.of('/img'); 

imgSpace.on('connection', (socket)=>{
  
    // socket refers to client side obj / event
  console.log(`New user connected :  \tSocket id \t ${socket.id} ` );
  
  console.log("Starting timer");
  var interval = setInterval(function() {		// save to var so can clear later
	//process.stdout.write(`waiting ${currentTime/1000} seconds`);		// repeating printout
	//console.log("Interval : Swap!");
	socket.emit('swap', 'NOW');
	}, 200);

		  	// * part 1 static
		  //socket.emit('message', { tommy:'Hey how are ya' });
		  // socket.on('another event', (data)=>{
		  //   console.log(data);
		  // });

  	// * part 2 messaging


  socket.on('message', (msg)=>{
  	console.log(`msg : ${msg}.`);
  	imgSpace.emit('message', ` msg : ${msg}`);
  });

  socket.on('disconnect',()=>{
  	console.log(' # # User disconnected.');
  	imgSpace.emit('message', ' # user disconnected # ' );
  });

});


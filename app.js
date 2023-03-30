const express = require('express'); // run Express
const chalk = require('chalk'); // chalk 5 is ESM if you want to use Chalk with TypeScript you should Chalk 4
const debug = require('debug')('app'); // and go to path at cmd and run : set DEBUG=* & node app.js (we run at cmd because terminal at vsc is a power shell so it's some difference command)
const morgan = require('morgan');
const path = require('path');

const app = express(); // call Express run app
const PORT = process.env.PORT || 4000; // set port

app.use(morgan('combined')); // use morgan
// show request?, windows?, os? information

app.use(express.static(path.join(__dirname, "/public/"))) // for use path that we specific -> tell where is static path -> directory path for tell where is express -> and use folder that keep static file

app.set("views", "./src/views"); // "./ is for tell that we want to access the folder"
app.set("view engine", "ejs"); // use view engine and call ejs for working

app.get("/", (req, res) => { // for manage request that comming at path "/", if they come in this page we will response something
    // res.send('Hello World'); // we will response txt 'Hello World'
    res.render('index', {username: "Young Lady", customer: ["Kitti", "Tanaphat", "YoungLady"]}); // when we use ejs we will use .render instead .sent // render to index.ejs and {data that we want to sent to ejs} --> for use dynamic web , and we can add not only str but array too
})

// app.listen(port, () => { // use for waitting for listen at port and do something when port is working
//     console.log("Listening on port " + chalk.green(port)) // show output at console.log
// })

app.listen(PORT, () => {
    debug("Listening on port " + chalk.green(PORT)) // show debug output
})

// at node.js can working on computer (outside web app) so you can run js at terminal directly
// by command : node app.js -> for running app
// and you can go at localhost:port in web browser too

// tool Chalk -> npm install chalk -> for set color output
// Debug -> watch debug at cmd
// Morgan -> Middleware ????????????
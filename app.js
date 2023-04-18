var express = require('express');
var app = express();

var bodyParser = require('body-parser');
var sumdisplay;
app.use(bodyParser.urlencoded({extended:false}));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html'); //Gets the html
});


app.get('/submission', function(req, res) {
  var first = parseInt(req.query.f);
  var second = parseInt(req.query.l);
  var sum = Number(first + second);
  sumdisplay = sum;
  console.log(sum)
  res.send('The sum is: ' + Number(sum));
  });



app.listen(3000);
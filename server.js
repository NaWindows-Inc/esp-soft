const http = require('http');


http.createServer(function (request, response) {
  var d = "";
  request.on('data', function (data) {
    d += data;
  });
  request.on('end', function () {
    now = new Date();
    console.log("%s: %s", now, JSON.stringify(JSON.parse(d), null, 1));
    response.end();
  });
}).listen(3000);
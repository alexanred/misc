var express = require('express'),
    summary = require('./summary');

var app = express();

app.configure(function () {
    app.use(express.logger('dev'));     /* 'default', 'short', 'tiny', 'dev' */
    app.use(express.bodyParser());
});


app.post('/summary', summary.psummary);
app.get('/summary', summary.gsummary);
app.listen(3000);
console.log('Listening on port 3000...');
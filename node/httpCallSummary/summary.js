exports.psummary = function(req, res) {
console.log("HTTP Method POST\n");
console.log(JSON.stringify(req.params));
console.log(JSON.stringify(req.headers));
console.log(JSON.stringify(req.body));

res.write("Method POST\n");
res.write("PARAMETERS "+   JSON.stringify(req.params));
res.write("HEADERS" + JSON.stringify(req.headers));
res.write("BODY"    + JSON.stringify(req.body));
res.end();

};

exports.gsummary = function(req, res) {

console.log("HTTP Method GET\n");
console.log(JSON.stringify(req.params));
console.log(JSON.stringify(req.headers));
console.log(JSON.stringify(req.body));

res.write("Method GET\n");
res.write("PARAMETERS "+   JSON.stringify(req.params));
res.write("HEADERS" + JSON.stringify(req.headers));
res.write("BODY"    + JSON.stringify(req.body));
res.end();

};

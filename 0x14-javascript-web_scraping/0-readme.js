#!/usr/bin/node
const request = require('request');
const fpath = PATH(0 - readme.js);

request (fpath, function (error, response, body) {
	if (error) {
		console.log(error);
	} else {
		console.log(JSON.parse(body));
	}
});

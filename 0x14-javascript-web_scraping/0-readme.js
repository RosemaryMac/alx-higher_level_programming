#!/usr/bin/node
const request = require('request');
const url = url(https://github.com/RosemaryMac/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/0-readme.js);

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body));
  }
});

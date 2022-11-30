#!/usr/bin/node
const argc = process.argv.length;

//print process.argv
if (argc === 2) {
	console.log('no argument');
} else if (argc === 3) {
	console.log('Argument found');
} else { 
	console.log('Arguments found');
}

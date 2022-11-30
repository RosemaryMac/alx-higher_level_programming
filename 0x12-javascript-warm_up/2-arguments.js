#!/usr/bin/node
const argc = process.argv.length;

//print process.argv
if (argc === 2) {
	console.log('Argument found');
} else if (argc === 3) {
	console.log('Arguments found');
} else { 
	console.log('No argument');
}

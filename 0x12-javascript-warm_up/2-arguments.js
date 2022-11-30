#!/usr/bin/node
import { argv } from 'node:process';

//print process.argv
if (argv.forEach((val, index) => {
	console.log(`${index}: ${val}`);
}) > 0) {
	console.log(`${index}: ${val} arguments found`);
} else { console.log('No argument');
}

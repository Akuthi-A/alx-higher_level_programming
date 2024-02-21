#!/usr/bin/node

let command = process.argv[2];

if (command === undefined)
{
	console.log("No argument");
}
else 
{
	console.log(command);
}

#!/usr/bin/node

let x_times = process.argv[2];

if (x_times === undefined)
{
	console.log("Missing number of occurrences");
}

for (let i = 0; i < x_times; i++)
{
	console.log("C is fun");
}

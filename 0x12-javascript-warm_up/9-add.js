#!/usr/bin/node

function add(a, b)
{
	let sum = a + b;
	console.log(sum);
}

add(Number(process.argv[2]), Number(process.argv[3]));

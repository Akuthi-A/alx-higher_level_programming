#!/usr/bin/node

function fact(n)
{
	if (n === 0 || n === 1 || isNaN(n))
	{
		return (1);
	}
	else
	{
		return (n * fact(n - 1));
	}
}

console.log(fact(process.argv[2]));

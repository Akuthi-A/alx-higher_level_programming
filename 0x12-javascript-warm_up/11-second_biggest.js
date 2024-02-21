#!/usr/bin/node

let args = process.argv.slice(2);

let nums = [];
for (let num in args)
{
	nums.push(Number(args[num]));
}

nums.sort(function(a, b) {
    return b - a;
});

if (process.argv.length < 3)
{
	console.log(1);
}
else
{
	console.log(nums[1]);
}

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement){
	let times = 0;

	for (elem of list)
	{
		if (elem === searchElement)
		{
			times += 1;
		}
	}

	return times;
}

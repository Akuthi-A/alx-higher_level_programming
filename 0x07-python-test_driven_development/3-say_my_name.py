#!/usr/bin/python3

"""
Defines the Say My Name function
"""


def say_my_name(first_name, last_name=""):
	"""
	This function takes 2 args, first and last name
	and prints -> ``My name is <first name> <last name>``

	args:
		first_name (str): first name
		last_name (str): last name

	Returns: Nothing
	Raises:
		TypeError: if either arg is not a string
	"""

	if not isinstance(first_name, str):
		raise TypeError("first_name must be a string\n")
        if not isinstance(last_name, str):
                raise TypeError("last_name must be a string\n")

	print(f"My name is {first_name} {last_name}\n")

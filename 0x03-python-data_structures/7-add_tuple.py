#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a < 2:
        rem = 2 - len_a
        zero_a = (0,) * rem
        tuple_a += zero_a

    if len_b < 2:
        rem = 2 - len_b
        zero_b = (0,) * rem
        tuple_b += zero_b

    var_a = tuple_a[0] + tuple_b[0]
    var_b = tuple_a[1] + tuple_b[1]

    return (var_a, var_b)

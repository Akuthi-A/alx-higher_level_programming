#!/usr/bin/python3

def multiple_returns(sentence):

    str_len = len(sentence)
    if str_len == 0:
        sentence = "None"
        return (str_len, sentence)
    else:
        first_char = sentence[0]
        return (str_len, first_char)

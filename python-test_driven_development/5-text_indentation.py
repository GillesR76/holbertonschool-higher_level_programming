#!/usr/bin/python3


"""
* Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
* Text must be a string, otherwise raise a TypeError
* There should be no space at the beginning or at the end
of each printed line
"""


def text_indentation(text):
    """
    Function that prints that prints a text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ch in ['.', '?', ':']:
        text = text.replace(ch, ch+"\n" * 2)
    text = text.rstrip("\n") and text.lstrip()
    text = text.rstrip()
    print(text.replace('\n ', '\n'), end="")

"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".


>>> backspace_compare("ab#c", "ad#c")
True
>>> backspace_compare("a##c", "#a#c")
True
>>> backspace_compare("a#c", "b")
False
"""


def get_result(string):
    stack = []
    for i in string:
        if i == "#":
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return stack


def backspace_compare(first: str, second: str):
    return get_result(first) == get_result(second)



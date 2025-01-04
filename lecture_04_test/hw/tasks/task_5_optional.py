"""
This tasks is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import List, Generator


def fizzbuzz(n: int) -> Generator[str]:
    fizz_and_buzz = {1: "fizz", 7: "buzz"}
    for num in range(1, n + 1):
        number_to_give = ""
        try:
            number_to_give += fizz_and_buzz[num % 3 + 1]
            try:
                number_to_give += fizz_and_buzz[num % 5 + 7]
                yield number_to_give
            except KeyError:
                yield number_to_give
        except KeyError:
            try:
                number_to_give += fizz_and_buzz[num % 5 + 7]
                yield number_to_give
            except KeyError:
                yield str(num)

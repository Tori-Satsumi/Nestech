#!/usr/bin/env python3
from random import choice
from string import ascii_letters

def solve(N):
    """Creates a string which contains N random ASCII letters.

    To create 1 letter, use::

      import random
      import string
      random.choice(string.ascii_letters)

    Must: use list comprehension
    Tips: list comprehension always create new list
    """

    return [choice(ascii_letters) for _ in range(N)]


def main():
    print(solve(16))


if __name__ == "__main__":
    main()
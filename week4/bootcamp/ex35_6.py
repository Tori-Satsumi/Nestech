#!/usr/bin/env python3
from operator import mul

def solve(N):
    """
    What is the sum of the digits of the number `2**1000`?
    https://projecteuler.net/problem=16

    Must: use list comprehension
    Tips: list comprehension always create new list
    """

    return mul([2 for _ in range(1000)])


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
#!/usr/bin/env python3


def solve(N):
    """Calculates sum of a list contains all integers less than N,
    which are multiple of 3 or 5.

    Given `sum` function:
    >>>  sum([1,2,3,4]) == 10

    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    return [ls for ls in [[i for i in range(1, _i)] for _i in range(1, N)] if (not (sum(ls) % 3) or not (sum(ls) % 5)) and ls]


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
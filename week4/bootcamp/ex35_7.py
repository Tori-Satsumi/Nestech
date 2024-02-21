#!/usr/bin/env python3


def solve(N):
    """Calculates sum of a list contains all integers less than N,
    which are multiple of 3 or 5.

    Given `sum` function:
    >>>  sum([1,2,3,4]) == 10

    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    lst = [[i for i in range(_i)] for _i in range(N)]
    return [ls for ls in lst if not sum(ls) % 3]

    return len([[i] for i in range(N) if not (sum([i]) % 3) or not (sum([i]) % 5)])


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
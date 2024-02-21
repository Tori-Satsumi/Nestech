#!/usr/bin/env python3


def solve(N):
    """Creates a list which contains N first even integers. ``[2, 4 ...]``
    Must: use list comprehension
    Tips: list comprehension always create new list
    """

    return [i for i in range(1, N + 1) if not i % 2]


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
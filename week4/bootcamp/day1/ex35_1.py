#!/usr/bin/env python3


def solve(N):
    """Create a list which contains N elements 2
    Must: use list comprehension
    Tips: list comprehension always create new list
    """

    return [2 for _ in range(N)]


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
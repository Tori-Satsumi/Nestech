#!/usr/bin/env python3


def solve(N):
    """Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
    """
    lst = [[f"{i}" * (N - 1)] for i in range(N)]
    for i, row in enumerate(lst):
        for ind, char in enumerate(lst[i]):
            if ind == i or ind == (N - 1 - i):
                continue
            else:
                lst[i][ind] = "*"

    for i in lst:
        print(i)

    return None


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
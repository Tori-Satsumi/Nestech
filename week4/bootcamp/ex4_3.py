#!/usr/bin/env python3
import string

def solve(words):
    """Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    """
    return list(map(points, map(str.lower, words)))

def points(word):
    points = 0
    for char in word:
        if char.isalpha():
            points += (ord(char) - 96)
    return points

def main():
    words = [
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
        "",
    ]

    print(solve(words))


if __name__ == "__main__":
    main()
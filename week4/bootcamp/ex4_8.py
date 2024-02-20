#!/usr/bin/env python3


def solve():
    """Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    """
    return {(_a, _b, _c) for _a in range(1, 11) for _b in range(1, 11) for _c in range(1, 11) if _a + _b + _c == 24}


def main():
    print(solve())


if __name__ == "__main__":
    main()
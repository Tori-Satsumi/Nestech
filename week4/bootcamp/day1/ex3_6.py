#!/usr/bin/env python3
from calendar import monthrange
from random import randint
import datetime

"""
Input: một số nguyên trong range(1,13,1). # start=1, stop=13, step=1
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
"""


def solve(input_data):
    """Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    (1,2) là biểu diễn tương tự [1,2], chỉ thay dấu ngoặc vuông thành tròn.
    Đây là kiểu dữ liệu tuple.
    :param input_data: tháng bất kì
    :rtype: list
    """
    mnt = randint(1, 12)
    return datetime.datetime(2018, mnt, 1).strftime("%B"), monthrange(2023, mnt)[1]


def main():
    month, day = solve(0)
    print(month, day)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

"""
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
"""

def fractional(num):
    if num == 1:
        return 1
    return num * fractional(num - 1)

def solve(input_data=10):

    return input_data


def main():
    print(solve())


if __name__ == "__main__":
    main()
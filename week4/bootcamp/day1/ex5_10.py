#!/usr/bin/env python3

"""
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
"""

def factorial(num):
    return 1 if num == 1 else num * factorial(num - 1)


def solve(input_data=10):
    return int(factorial(input_data * 2) / (factorial(input_data) ** 2))


def main():
    print(solve(5))


if __name__ == "__main__":
    main()
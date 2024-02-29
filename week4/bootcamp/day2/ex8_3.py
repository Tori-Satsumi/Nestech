#!/usr/bin/env python3


from typing import List
import string

data = ["nhung", "bong", "hoa", "nho", "va", "nhung", "bong", "hoa", "to"]


def change(iterable: List) -> List[str]:
    """Trả về list chứa các phần tử của iterable đã chuyển thành chữ HOA
    Không dùng list comprehension, for.

    Gợi ý:
        iterator, while, try/except

    :param input_data: dữ liệu sử dụng iterable
    :rtype list:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    return map(string.upper(), )

def solve(input_data):
    # function `solve` dành cho mục đích `test`, không cần sửa
    # Gía trị trả về của `solve` và `your_function` là như nhau
    return change(input_data)


def main():
    words = data
    result = solve(words)
    assert isinstance(result, list)
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
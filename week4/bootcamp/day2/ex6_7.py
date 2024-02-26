#!/usr/bin/env python3


def solve(input_data):
    """
    Trả về string biễu diễn tương ứng ở hệ thập phân (decimal),
    hệ nhị phân (binary), bát phân (octal), thập lục phân (heximal)

    Gợi ý: sử dụng bin(), oct(), hex(), string method `rjust`
    Mỗi dòng 1 số, với độ rộng là 8, các giá trị thẳng nhau căn lề phải.
    Output :

       1       1     0o1     0x1
       2      10     0o2     0x2
       ...
    """
    return [str(num).rjust(4) + bin(num).rjust(8) + oct(num).rjust(8) + hex(num).rjust(8) for num in input_data]


def main():
    input_data = range(1, 20)
    # print(solve(input_data))
    for i in solve(input_data):
        print(i)

if __name__ == "__main__":
    main()
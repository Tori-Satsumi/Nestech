#!/usr/bin/env python3


def sumall(*input_data):
    """Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
    """
    
    return sum([round(float(i), 2) for i in input_data if check_num(i)])


def check_num(num):
    try:
        _ = int(float(num)) 
        return True
    except:
        return False


def solve():
    lst = [
        10,
        10.2,
        10.,
        .0,
        ".7",
        "abc",
        r".1",
    ]

    return sumall(*lst)


def main():
    print(solve())


if __name__ == "__main__":
    main()
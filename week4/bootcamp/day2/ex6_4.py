#!/usr/bin/env python3


def sumall(*input_data):
    """Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
    """
    
    return sum([round(float(i), 2) for i in input_data if str(i).isnumeric()])

def convert_flt(num):
    try:
        num = int(float(num)) 
        return True
    except:
        return False


def solve():

    return None


def main():
    print(solve())


if __name__ == "__main__":
    main()
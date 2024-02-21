#!/usr/bin/env python3

import time


def solve():
    """Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66
      a + 13 * b / c + d + 12 * e - f      + g * h / i      = 87
    """

    cnt = 0
    start = time.time()

    # 4.5s
    # amount of value: 447485
    f1 = {}
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                fnc1 = str(a + 13 * b / c)
                f1[fnc1] = f1[fnc1] + 1 if fnc1 in f1 else 1

    f2 = {}
    for d in range(1, 10):
        for e in range(1, 10):
            for f in range(1, 10):
                fnc2 = str(d + 12 * e - f)
                f2[fnc2] = f2[fnc2] + 1 if fnc2 in f2 else 1

    f3 = {}
    for g in range(1, 10):
        for h in range(1, 10):
            for i in range(1, 10):
                fnc3 = str(g * h / i)
                f3[fnc3] = f3[fnc3] + 1 if fnc3 in f3 else 1


    for key1, value1 in f1.items():
        for key2, value2 in f2.items():
            for key3, value3 in f3.items():
                if float(key1) + float(key2) + float(key3) == 87:
                    cnt += int(value1) * int(value2) * int(value3)


    # 88 sec
    # amount of value: 442232
    # for a in range(1, 10):
    #     for b in range(1, 10):
    #         for c in range(1, 10):
    #             for d in range(1, 10):
    #                 for e in range(1, 10):
    #                     for f in range(1, 10):
    #                         for g in range(1, 10):
    #                             for h in range(1, 10):
    #                                 for i in range(1, 10):
    #                                     if a + 13 * b / c + d + 12 * e - f + g * h / i == 87:
    #                                         cnt += 1

    print(f"time: {time.time() - start} sec")
    return cnt


def main():
    print(solve())


if __name__ == "__main__":
    main()
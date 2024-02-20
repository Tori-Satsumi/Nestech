#!/usr/bin/env python3
import time
from random import randrange, randint

def solve(numbers, mode="merge"):
    """Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`

    Gợi ý: python có sẵn giá trị âm/dương vô cùng.
    """
    assert isinstance(numbers, list)

    if len(numbers) > 2:
        if mode == "merge":
            """
            merge sort
            """
            lst = divide_ls(numbers)
            while len(lst) > 1:
                lst = list(map(sort_ls, add_ls(lst)))

            return list(map(sort_ls, lst))[0][0]
        elif mode == "bubble":
            """
            bubble sort
            """
            return sort_ls(numbers)[0]

    elif len(numbers) == 2:
        return numbers[1] if numbers[0] < numbers[1] else numbers[0]
    else:
        return numbers


"""
add 2 small lists contain 2 or less element together
require: big list
"""
def add_ls(lst: list):
    hld = []
    for i in range(0, len(lst), 2):
        if i == len(lst) - 1:
            hld.append(lst[i])
        else:
            hld.append(lst[i] + lst[i + 1])
    return hld


"""
divide list into small list contain 2 element
require: big list
"""
def divide_ls(lst: list):
    return [lst[_t: _t + 2] for _t in range(0, len(lst), 2)]

"""
sort the entire list
require: small list
"""
def sort_ls(lst: list):
    hld = lst
    while True:
        done = True
        for i1 in range(len(hld)):
            num = hld[i1]
            index = i1
            
            for i2 in range(i1, len(hld)):
                if num < hld[i2] and index < i2:
                    num = hld[i2]
                    index = i2
                    done = False

            hld[index] = hld[i1]
            hld[i1] = num
        if done:
            return hld

def random_list():
    size = randint(1000, 10000)
    return [ randint(0, size) for _ in range(size)]


def main():
    a = [-1, 5, 9, 6, -999999999999999, 1]
    b = random_list()
    print(f"len random list: {len(b)}")

    start = time.time()
    print(solve(b, "bubble"))
    print(f"end: {time.time() - start}")


if __name__ == "__main__":
    main()
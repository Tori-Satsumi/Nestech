#!/usr/bin/env python3

# lst = []
def divide_ls(iterable, N):
    # from ex4_9.py func divide_ls
    return [iterable[_t: _t + N] for _t in range(0, len(iterable), N)]


def solve(iterable, N):
    """Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    """
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Bạn chưa làm bài này")

    # sửa thành tên function phù hợp
    result = divide_ls(iterable, N)

    return result


def main():
    li = ["meo", "bo", "ga", "cho", "chim", "gau", "voi"]
    print(solve(li, 2))


if __name__ == "__main__":
    main()
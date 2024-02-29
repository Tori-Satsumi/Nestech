#!/usr/bin/env python3
from datetime import datetime, date
import math
__doc__ = """
Viết script get_version nhận vào ngày ở format <month>/<day>/<year>.
VD: 03/28/16 làm parameter và in ra một version được tính theo quy luật sau:
- Version ở dạng format: <MAJOR>.<MINOR>.<PATCH>, vd: "6.9.2"
- Cách đánh version này gọi là semver http://semver.org/
- Từ ngày 09 tháng 02 năm 2016, phiên bản bắt đầu là "1.0.0"
- Mỗi 28 ngày, MAJOR lại tăng thêm 1, MINOR và PATCH set về 0
- Mỗi 7 ngày, MINOR tăng thêm 1 và PATCH sẽ set về 0
- Cứ mỗi ngày, PATCH lại tăng thêm 1.

In ra phiên bản tương ứng.

Gợi ý: sử dụng `sys.argv` hoặc module `argparse`
https://pymotw.com/3/argparse/index.html
"""

# import logging

# logger = logging.getLogger(__name__)

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, r"%m/%d/%y").strftime(r'%m/%d/%y'):
            raise ValueError
        return True
    except ValueError:
        return False


def get_version(input_data: str) -> str:
    """Trả về tên phiên bản như yêu cầu tại ``__doc__``

    :param input_data: ngày format ở dạng <month>/<day>/<year>,
                       ví dụ: "02/03/16"
    :rtype str:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    if validate(input_data):
        m, d, y = input_data.split("/")
        gap = abs(int((datetime(2016, 2, 9) - datetime(int(f"20{y}"), int(m), int(d))).days))

        major = 0
        minor = 0
        patch = 0
        for _ in range(gap):
            if minor == 4:
                minor = 0
                patch = 0
                major += 1
                continue

            if patch == 7:
                minor += 1
                patch  = 0
                continue

            patch += 1

        return f"{major}.{minor}.{patch}"

    else:
        raise ValueError("Invalid date")


def solve(input_data):

    """Function `solve` dùng để `test`, không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :rtype str:
    """
    result = get_version(input_data)
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Bạn chưa làm bài này")
    return result


def main():
    # input_data = None

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu
    # vào biến `input_data`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("chưa thực hiện truyền input_data")

    # logger.debug("Getting version for the day %s", input_data)
    # print(input_data, solve(input_data))

    for d in "02/03/16", "09/06/16", "06/23/17":
        print(d, solve(d))


if __name__ == "__main__":
    main()
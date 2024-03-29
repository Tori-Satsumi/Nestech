#!/usr/bin/env python3

__doc__ = """
Yêu cầu:
- Tìm và in ra tổng số dòng của mỗi loại file (kể cả thư mục con,
dựa vào phần mở rộng abc.py và xyz.py là cùng loại) khi thực hiện lệnh:

    ex8_9.py `duong_dan_toi_thu_muc`

- Mặc định là thư mục hiện tại: PATH = '.'

Gợi ý: sử dụng `os.walk` để duyệt vào thư mục con.

Yêu cầu nâng cao:
- Trong thư mục hiện tại nếu tìm thấy file là python module
in ra màn hình tên của các function trong đó

Gợi ý: sử dụng 2 module `inspect` và `importlib`
``from inspect import isfunction``
``from importlib import import_module``

Tham khảo thêm cho Sysadmin

- Explore more stdlib for system: os, shutil, subprocess, thread, multiprocess,
  smtp, imap, pop3
- Explore 3rd lib: psutils, paramiko, twisted, gevent
- Use tools written in python: diamond, graphite, saltstack, odoo, sentry,
  fabric, shinken, django CMS, trac, buildbot
"""


# import log
from typing import Dict
import os
from inspect import isfunction
from importlib import import_module

# logger = log.get_logger(__name__)
# PATH = "."


def your_function(path) -> Dict[str, int]:
    """Trả về `dict` chứa tổng số dòng của từng loại file trong thư
    mục hiện tại (bao gồm cả thư mục con) theo format:

        result = {
            ".py": 1234,
            ".txt": 5678,
            ...
        }

    Lưu ý:
    - Nếu file không đọc được, gán số dòng bằng 0

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = {}
    module_name = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            try:
                nm, ext = name.rsplit(".", 1)
            except:
                result[name] = 0
                continue

            try:
                with open(name, "r") as fle:
                    ln = len(list(fle))
                    result[ext] = result[ext] + ln if ext in result else ln
            except:
                result[ext] = 0

            if ext == "py":
                """                
                TODO: remove try except
                really dont need the try except here
                just to be safe
                """
                try:
                    module = import_module(nm)
                    module_name[name] = [func for func in dir(module) if isfunction(getattr(module, func))]
                except:
                    pass

    print("\n\n")
    for key, value in result.items():
        print(f"{key} file extension has {value} line(s) of code")
    print("\n\n")
    for key, lst in module_name.items():
        print(f"{key} has: {len(lst)} user made function(s) \ninclude: \n{' | '.join(lst)} \n")

    print("\n\n")


    return None



def solve(input_data):
    """Function `solve` dùng để `test`, không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    NOTE: nếu test xảy ra exception, mở file test và sửa lại cho đúng,
    bạn đã học hết Python rồi.
    """

    # logger.debug("Statically analysing directory %s", input_data)
    result = your_function(input_data)
    return result


def main():
    # path = PATH  # thư mục hiện tại
    path = '.'
    
    # the core dir link, use this and ur code will go thru the entire laptop memory, gonna take a few mins - hours to complete
    # path = '\' 

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu vào biến `path`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("chưa thực hiện truyền `path`")

    print(solve(path))


if __name__ == "__main__":
    main()


# chưa duyệT đc thư mục con
# chưa xử lý đc file ko đọc đc
#!/usr/bin/env python3

import os
import sys

def solve(*args, **kwargs):
    """Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    """

    # for os.py is in home folder, we will start there
    # Đường dẫn tới code của module `os`
    lst_att = []
    for root, dirs, files in os.walk("/home"):
        for file in files:
            try:
                name, ext = file.rsplit(".", 1)
            except:
                continue

            if name == "os" and ext == "py":
                ...

    return None


def main():
    print(solve())


if __name__ == "__main__":
    main()
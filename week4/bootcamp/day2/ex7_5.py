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

    """
    hint: os.py is in:
    /home/codespace/.python/current/lib/python3.10
    or 
    /usr/local/python/3.9.18/lib/python3.9
    """    
    # Đường dẫn tới code của module `os`
    path = ()
    for root, dirs, files in os.walk("/"):
        for file in files:
            if file == "os.py":
                path = root
                break
        if path:
            break

    print(path)

    return None


def main():
    print(solve())


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# import re

def solve(text):
    """Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    """

    # use isalnum()

    # if srch := re.findall(r"(\d+)", text):
    #     return srch
    # else:
    #     return None

    hld = ""
    ls = []
    for char in text:
        if char.isnumeric():
            hld += char
        elif hld:
            ls.append(hld)
            hld = ""
    if hld: 
        ls.append(hld)
    return ls

def main():
    ss = "Bé lên 3 bé đi lớp 4"
    ss = "Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu9"
    print(solve(ss))
    # assert solve(ss) == [3, 4]


if __name__ == "__main__":
    main()
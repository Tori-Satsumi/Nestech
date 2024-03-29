#!/usr/bin/env python3


data = {
    "green": "#3cba54",
    "yellow": "#f4c20d",
    "red": "#db3236",
    "blue": "#4885ed",
}


def solve(colors):
    """Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    """
    txt = "Google"
    color = ["blue", "red", "yellow", "blue", "green", "red"]

    return list(zip(list(txt), [data[clr] for clr in color]))


def main():
    """Biết mã hex của các màu trong Google logo là:"""
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()
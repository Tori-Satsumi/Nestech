#!/usr/bin/env python3

import os
import json  # NOQA
import urllib.request

data = os.path.join(os.path.dirname(__file__), "salt_contributors.json")


def read_api(datapath="https://api.github.com/repos/saltstack/salt/contributors?page=4"):
    """Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, html_url và contributions.
    Nếu html_url nào bị thiếu, tạo html_url mới bằng
    "https://github.com/" + login tương ứng.
    """
    with urllib.request.urlopen(datapath) as url:
        data = json.load(url)
        with open("info.json", "w") as jsfile:
            json.dump(data, jsfile, indent=4)


    return None
    


def solve():
    # read_api()
    with open("info.json", "r") as file:
        data = file.load()
        for row in data:
            print(row)

    return None

def main():
    """Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=4 Lưu lại
    thành file salt_contributors.json.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    File đã được lưu sẵn trong thư mục này - link để đây để biết
    dữ liệu lấy từ đâu.
    """
    datafile = data

    for d in solve():
        print("User: {login} - URL {html_url} - {contributions}".format(**d))


if __name__ == "__main__":
    main()
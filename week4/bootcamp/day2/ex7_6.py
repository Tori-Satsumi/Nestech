#!/usr/bin/env python3
"""
Chú ý bảo mật: bài này chỉ để minh họa ý tưởng, không sử dụng code này để
sinh mật khẩu. Lý do: random chỉ là giả ngẫu nhiên (pseudo random),
không phải ngẫu nhiên thật,
nên mật khẩu sinh ra có thể bị hacker đoán được.
Để sinh mật khẩu thực sự ngẫu nhiên, xem thư viện
secret https://docs.python.org/3.7/library/secrets.html
"""

import random  # NOQA
import string  # NOQA
import secrets

full_list = string.ascii_letters + string.punctuation + string.digits

def your_function(length=16):
    """Tạo một mật khẩu ngẫu nhiên (random password),
    mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
    1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
    """



def generate_and_append(length, passwords=[]):
    """
    Sinh password ngẫu nhiên và append vào list passwords.
    Nếu không có list nào được gọi với function, trả về list chứa một
    password vừa tạo ra.
    Sửa argument tùy ý.
    """

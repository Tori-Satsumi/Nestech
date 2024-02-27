#!/usr/bin/env python3
from random import randint

"""
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

Đọc file class.md trong thư mục này.
"""


class Fighter:
    def __init__(self, name, initial_health=100) -> None:
        self.name = name
        self.maxhealth = initial_health
        self.health = initial_health

    def __str__(self) -> str:
        return f"{self.name} has {self.health}/{self.maxhealth} left"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("No name given")
        self._name = name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def maxhealth(self):
        return self._maxhealth

    @maxhealth.setter
    def maxhealth(self, initial_health):
        self._maxhealth = initial_health

    def take_dmg(self, dmg_taken):
        self.health -= dmg_taken

    def deal_dmg(self):
        return randint(1, 10)

class Weapon:
    ...

def solve(player1, player2):
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""
    result = None

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Nguyễn Phương Hằng', 1000)
    player2 = Fighter('Thuỷ Tiên', 100)
    print(solve(player1, player2))


"""
NOTE
sau khi thành thạo việc tạo 1 class và viết method, có thể
vào link sau lấy chứng chỉ Python basic của HackerRank
Rất dễ, làm 5-10 phút là xong.

https://www.hackerrank.com/skills-verification/python_basic
"""


if __name__ == "__main__":
    main()
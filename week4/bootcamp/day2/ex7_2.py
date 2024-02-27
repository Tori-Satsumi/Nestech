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

class Special:
    def __init__(self) -> None:
        self.ability = self.perk

    def perk(self):
        ability = ["heal", "ex_crit", "life_stl"]
        return ability[randint(0, 3)]


class Weapon():
    def __init__(self, level) -> None:
        self.player_lvl = level
        self.crit_hit_req = 0

    def deal_dmg(self):
        if self.crit_hit_req >= 5:
            self.crit_hit_req = 0
            return 20 * self.player_lvl
        
        return randint(self.player_lvl, 10 + self.player_lvl)

    def crit_require(self, hit):
        self.crit_hit_req = hit


class Fighter(Weapon):
    def __init__(self, name, initial_health=100, level=0, defendpoint=0) -> None:
        super().__init__(level)
        self.name = name
        self.maxhealth = initial_health
        self.health = initial_health
        self.level = level
        self.defendpoint = defendpoint

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

    def take_dmg(self, dmg_taken):
        dmg = dmg_taken * (100 - self.defendpoint) / 100
        if (dmg / self.maxhealth) * 100 > 0.1:
            super().crit_require(round(self.maxhealth / dmg, 0))
        self.health -= dmg


def solve(player1, player2):
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""

    while player1.health > 0 and player2.health > 0:
        player1.take_dmg(player2.deal_dmg)
        player2.take_dmg(player1.deal_dmg)
    
    return (player1.name, player1.health) if player1.health > 0 else (player2.name, player2.health)
        




def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Nguyễn Phương Hằng', 1000, 3, 30)
    player2 = Fighter('Thuỷ Tiên', 100, 2, 85)
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
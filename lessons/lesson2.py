# наследование
# родительский\ супер Класс
class Hero:
    def __init__(self, nickname, lvl, hp):
        # Атрибуты класса, функционал как у переменных
        self.nick_name = nickname
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return self.nick_name

#дочерний класс
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Я потомок {self.nick_name}"

class WarriorHero(Hero):
    def __init__(self, name, lvl, hp, damage):
        super().__init__(name, lvl, hp)
        self.damage = damage
obj_1 = Hero("Oleg", 10, 100)
obj_2 = MageHero("Ardager", 100, 1000, 50)
obj_3 = WarriorHero("Axe", 15, 1200, 87)
print(obj_1.action())
print(obj_2.nick_name, obj_2.mp)
print(obj_3.damage)
#Класс
class Hero:
    # Конструктор класса
    def __init__(self, nickname, lvl, hp):
        # Атрибуты класса, функционал как у переменных
        self.nick_name = nickname
        self.lvl = lvl
        self.hp = hp
        #Методы класса
    def action(self):
     return f"{self.nick_name} Hi this is my base action!!"

#объекты\экземпляр класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100, 700)

print(kirito.action())
print(asuna.action())


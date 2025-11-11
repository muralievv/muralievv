# class Animal:
#     def __init__(self, name: str, age: int, health: int):
#         self.name = name
#         self.age = age
#         self.health = health
#     def info(self) -> str:
#         return(f"{self.name}, {self.age} years old, {self.health} hp")
#     def use_ability(self):
#         return f"{self.name}uses basic ability."
# class Flyable:
#     def use_ability(self):
#         return super().use_ability() + " Can fly."
# class Swimmable:
#     def use_ability(self):
#         return super().use_ability() + " Can swim."
# class Invisible:
#     def use_ability(self):
#         return super().use_ability() + " Can be invisible."
# class Duck(Flyable, Swimmable, Animal):
#     pass
# class Bat(Flyable, Invisible, Animal):
#     pass
# class Frog(Swimmable,Animal):
#     pass
# class Phoenix(Flyable, Animal):
#     def reborn(self):
#         return f"{self.name} Reborn."
# class Zoo:
#    def __init__(self):
#        self.animals = []
#    def add_animal(self, animal: Animal):
#        self.animals.append(animal)
#    def show_all(self):
#         return "\n".join(animal.info() for animal in self.animals)
#    def perform_show(self):
#         return "\n".join(animal.use_ability() for animal in self.animals)
# if __name__ == "__main__":
#     zoo = Zoo()
#
#     duck = Duck("Дональд", 3, 80)
#     bat = Bat("Бэтти", 5, 60)
#     frog = Frog("Кермит", 2, 50)
#     phoenix = Phoenix("Феникс", 100, 200)
#
#     for animal in (duck, bat, frog, phoenix):
#         zoo.add_animal(animal)
#
#     print(f"=== Информация о животных ===,\n{zoo.show_all()}")
#
#     print(f"\n=== Шоу суперспособностей ===\n{zoo.perform_show()}")
#
#     print("\nMRO для Duck:", Duck.__mro__)
#     print("MRO для Phoenix:", Phoenix.__mro__)
#
#
#
# from turtle import *
# pensize(10)
# while True:
#     forward(1)
#     left(1)
#     right(1)
#     back(1)
# class Hero:
#     def __init__(self, name, age, speed):
#         self.name = name
#         self.age = age
#         self.speed = speed
#     def opisanie(self):
#         return f"{self.name}, {self.age} years old, {self.speed}/100"
#     def change_mood(self):
#         return f"Nastroenie geroya {self.name} izmenilos na plohoe"
# Kirito = Hero("Kirito", 18, 88)
# print(Kirito.opisanie())
# print(Kirito.change_mood())

class Animal:
   def __init__(self, name: str, age: int, health: int):
       self.name = name
       self.age = age
       self.health = health      # очки здоровья

   def info(self) -> str:
       return f"{self.name}, {self.age} лет, здоровье {self.health}"

   def use_ability(self) -> str:
       """Переопределяется в наследниках"""
       return f"{self.name} использует базовую способность."
class Flyable:
    def use_ability(self):
        return super().use_ability() + " Can fly"





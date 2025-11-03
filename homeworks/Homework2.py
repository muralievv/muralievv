class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self) -> str:
        return f"{self.name}, {self.age} years old, {self.health}hp."
    def use_ability(self) -> str:
        return f"{self.name}, uses basic ability"
class Flyable:
    def use_ability(self) -> str:
        return f"{self.name} can fly"
class Swimmable:
    def use_ability(self) -> str:
        return f"{self.name} can swim"
class Invisible:
    def use_ability(self) -> str:
        return f"{self.name} can be invisible"
class Duck(Flyable,Swimmable, Animal):
    def use_ability(self):
        return f"{self.name } Uses basic ability. Can swim. Can fly."
class Bat(Animal,Flyable):
    def use_ability(self):
        return f"{self.name} Uses basic ability. Can fly. Can be invisible."
class Frog(Animal,Swimmable):
    def use_ability(self):
        return f"{self.name} Uses basic ability. Can swim."
class Phoenix(Flyable,Invisible, Animal):
    def use_ability(self):
        return f"{self.name} Uses basic ability. Can fly. Can be invisible."
class Zoo():
    def add_animal(self, animal: Animal):
        self.animals.append(animal)
    def __init__(self):
        self.animals = []
    def show_all(self):
        return "\n".join(animal.info() for animal in self.animals)
    def perform_show(self):
        return "\n".join(animal.use_ability() for animal in self.animals)
if __name__ == "__main__":
   zoo = Zoo()
   duck = Duck("Donald", 3, 80)
   bat = Bat("Batty", 5, 60)
   frog = Frog("Froggy", 2, 50)
   phoenix = Phoenix("Phoenix", 100, 200)

   for animal in (duck, bat, frog, phoenix):
       zoo.add_animal(animal)

   print(f"=== Информация о животных ===\n{zoo.show_all()}")

   print(f"\n=== Шоу суперспособностей ===\n{zoo.perform_show()}")
   print("\nMRO для Duck:", Duck.__mro__)
   print("MRO для Phoenix:", Phoenix.__mro__)

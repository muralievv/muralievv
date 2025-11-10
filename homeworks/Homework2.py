class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self) -> str:
        return f"{self.name}, {self.age} years old, {self.health}hp."
    def use_ability(self) -> str:
        return f"{self.name}, uses basic ability."
class Flyable:
    def use_ability(self) -> str:
        return super().use_ability() + " Can fly"
class Swimmable:
    def use_ability(self) -> str:
        return super().use_ability() + " Can swim."
class Invisible:
    def use_ability(self) -> str:
        return super().use_ability() + " Can be invisible."
class Duck(Flyable,Swimmable, Animal):
    pass
class Bat(Flyable,Invisible,Animal):
    pass
class Frog(Swimmable, Animal):
    pass
class Phoenix(Flyable,Invisible, Animal):
    def reborn(self):
        return f"{self.name} Reborn."
class Zoo:
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

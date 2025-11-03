class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self) -> str:
        return f"{self.name}, {self.age}, {self.health}"
    def use_ability(self) -> str:
        return f"{self.name} uses basic ability"
class Flyable:
    def use_ability(self) -> str:
        return f"{self.name}  can fly"
class Swimmable:
    def use_ability(self) -> str:
        return f"{self.name} can swim"
class Invisible:
    def use_ability(self) -> str:
        return f"{self.name} can be invisible"
class Duck(Animal, Flyable, Swimmable):
    def use_ability(self) -> str:
        return f"{self.name} can swim and fly"
class Bat(Animal, Flyable):
    def use_ability(self) -> str:
        return f"{self.name} can fly"
class Frog(Animal, Swimmable):
    def use_ability(self) -> str:
        return f"{self.name} can swim"
class Phoenix(Animal,Flyable, Invisible):
    def use_ability(self) -> str:
        return f"{self.name} can fly and be invisible"
class Zoo:
    def add_animal(self, animal: Animal):
        self.animals.append(animal)
    def __init__(self):
        self.animals = []
    def info(self):
        return "\n".join(animal.info() for animal in self.animals)
    def use_ability(self):
        return "\n".join(animal.use_ability() for animal in self.animals)
if __name__ == "__main__":
        zoo = Zoo()

        duck = Duck("Donald", 3, 80)
        bat = Bat("Batty", 5, 60)
        frog = Frog("Froggy", 2, 50)
        phoenix = Phoenix("Phoenix", 100, 200)

        for animal in (duck, bat, frog, phoenix):
            zoo.add_animal(animal)

        print(f"=== Информация о животных === \n{zoo.info()}")

        print(f"\n=== Шоу суперспособностей ==={zoo.use_ability()}")

        print("\nMRO для Duck:", Duck.__mro__)
        print("MRO для Phoenix:", Phoenix.__mro__)
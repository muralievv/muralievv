class Car:
    def __init__(self, name, horsepower, weight):
        self.name = name
        self.horsepower = horsepower
        self.weight = weight
    def description(self):
        return f"{self.name}, {self.horsepower} hp, {self.weight} kg"
    def boost_horsepower(self):
        self.horsepower += 50
        return f"the {self.name} power increased by 50 hp. Now it is {self.horsepower} hp"
HyundaiPalisade = Car("Palisade", 291, 2050)
SubaruForester = Car("Forester", 182, 1600)
print(HyundaiPalisade.description())
print(SubaruForester.description())
print(HyundaiPalisade.boost_horsepower())
print(SubaruForester.boost_horsepower())
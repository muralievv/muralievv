#Магический метод
class Test:
    #double underline
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
test_obj = Test("test")
print(test_obj)
class Book:
    def __init__(self, title: str, author: str, pages: int, format = 'бумажная'):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format
    def __str__(self,): #маг метод строчки
        return f'"{self.title}": {self.author}, {self.pages} страниц, {self.format}'
    def __len__(self): #маг метод подсчитывания
        return self.pages
    def __add__(self, other):#маг метод для сложения
        return (self.pages + other.pages)
    def __eq__(self, other): #маг метод сравнения
        if book1.pages == book2.pages:
            return True
        else:
            return False
    def __getitem__(self, item): #маг метод который позволяет взять что-то по индексу
        return f"Глава {[item]}: содержание книги '{self.title}'"
    @classmethod
    def from_string(cls, s: str): #метод класса который позволяет работать с классом, а не с объектами
        title, author, pages = s.split(", ")
        return cls(title, author, int(pages))

    @staticmethod
    def is_thick(pages: int): #стат метод который позволяет работать независимо ни от чего
        if pages >= 500:
            return True
        else:
            return False

book1 = Book("1984", "Дж. Оруэлл", 328, )
book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")
print(book1)
print(len(book1))
print(book1 + book2)
print(book1 == book2)
print(book1[5])
print(Book.is_thick(600))
print(Book.is_thick(300))
book3 = Book("Python", "Гвидо", 200)
print(book3.format)
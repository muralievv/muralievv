# Инкапсуляция

import random
import string

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name  # открытая
        self._balance = balance  # защищённый атрибут
        self.__password = password  # приватный атрибут

    def login(self, password):
        if self.__password == password:
            print("Вы вошли!!")
        else:
            print("Неверный пароль!!")

    def get_balance(self, password):
        if self.__password == password:
            return self._balance
        else:
            return "Неверный пароль!!"

    def __random_pass(self):
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(6))
        return password

    def get_new_pass(self):
        return self.__random_pass()


# Создание объекта
john = BankAccount("John", 100, "123qwerty")

john.login("123321")
print(john.get_balance("123qwerty"))
print(john.get_new_pass())


# Абстрактные классы
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Gaf Gaf"

    def move(self):
        return "Step"


gufi = Dog()
print(gufi.make_sound())


# Пример использования абстрактного класса для SMS
class SmsSend(ABC):
    @abstractmethod
    def send_otp(self):
        pass


class KGSms(SmsSend):
    def send_otp(self):
        text = "<text>1234</text>"
        phone = "<phone>+996779</phone>"
        self.send_sms(text, phone)

    def send_sms(self, text, phone):
        print(f"Отправка SMS KG: {text} -> {phone}")


class RUSms(SmsSend):
    def __init__(self, text):
        self.text = text

    def send_sms(self, data):
        print(f"Отправка SMS RU: {data}")

    def send_otp(self):
        data = {
            "text": self.text,
            "phone": "+7925"
        }
        self.send_sms(data)


kg_sms = KGSms()
kg_sms.send_otp()

ru_sms = RUSms("Ваш код: 4321")
ru_sms.send_otp()

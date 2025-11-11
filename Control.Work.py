class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"
class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp,):
        super().__init__(name, lvl, hp, mp=0)
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"
class BankAccount:
    bank_name = "Simba"  # атрибут класса

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance      # защищённый
        self.__password = password   # приватный
    def login(self, password):
        if password == self.__password:
            print("Вы успешно вошли!")
        else:
            print("Неправильный пароль!")

 # Свойство full_info (только для чтения)
    @property
    def full_info(self):
        return f"{self.hero}: Баланс: {self._balance} Сом"
  # Классовый метод
    @classmethod
    def get_bank_name(cls):
        return f"Банк:{cls.bank_name}"
# Статический метод: расчёт бонуса за уровень
    @staticmethod
    def bonus_for_level(lvl):
        if lvl >= 50:
            return f"Бонус за {lvl} уровень: 500 сом"
        else:
            return f"Бонус за {lvl} уровень: 250 сом"
    def __str__(self):
        return f"{self.hero}, Баланс: {self._balance}SOM"
    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return f"Общий баланс: {self._balance + other._balance} SOM"

        else:
            return f"Формат типа героев не совпадает."
    def __eq__(self, other):
        return self.hero == other.hero and self._balance == other._balance
from abc import ABC, abstractmethod

class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass
class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"
class RusSms(SmsService):
    def send_otp(self, phone):
        return f'"text" Код: "1234" "phone": "{phone}"'



kg_sms = KGSms()
ru_sms = RusSms()
merlin = MageHero("Merlin", 12, 200, 150)
conan = WarriorHero("Conan", 50, 400)
merlin1 = BankAccount("Merlin", 5000, "zxcqwe123")
conan1 = BankAccount("Conan", 3000, "qwezxc123")
print(merlin.action())
print(conan.action())
print(merlin1.full_info)
print(conan1.full_info)
print(BankAccount.get_bank_name())
print(merlin1.bonus_for_level(50))
print(conan1.bonus_for_level(49))
print(merlin1)
print(conan1)
print(merlin1 + conan1)
print(merlin1 == conan1)
print(kg_sms.send_otp(+996777123456))
print(ru_sms.send_otp(+701072007192))




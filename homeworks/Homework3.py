import random
import string


class BankAccount:
   def __init__(self, name, balance, password):
       self.name = name                 # открытый
       self._balance = balance          # защищённый
       self.__password = password       # приватный
   def deposit(self, amount, password):
       if self.__password == password:
           self._balance += amount
           return self._balance
       else:
           return "Неверный пароль!"
   def withdraw(self, amount, password):
       if self.__password == password and self._balance >= amount:
           self._balance -= amount
           return self._balance
       elif self.__password != password:
           return "Неверный пароль!"
       else:
           return "Недостаточно средств!"
   def change_password(self, old_password, new_password):
       self.old_password = old_password
       self.new_password = new_password
       if self.old_password == self.__password:
           new_password = input("Введите новый пароль: ")
           self.__password = new_password
           return "Пароль изменён"
       else:
           return "Старый пароль неверный!"
   def get_balance(self, password):
       if password == self.__password:
           return self._balance
       else:
           return "Пароль неверный"
   def reset_pin(self, password):
       numbers = string.digits
       password = ''.join(random.choice(numbers) for _ in range(4))
       if password == password:
        return password
       else:
           return 'Неверный пароль!'

from abc import ABC, abstractmethod
class NotificationSender(ABC):
   @abstractmethod
   def send(self, message, recipient):
       pass
class EmailSender(NotificationSender):
    def __init__(self, service = "Gmail"):
        self._service = service
    def send(self, message, recipient):
        return f"Email sent to {recipient}"
    def get_service(self):
        return f'Сервис: {self._service}'
class SmsSender(NotificationSender):
    def __init__(self, service = "Twilio"):
        self._service = service
    def send(self, message, recipient):
        return f"Sms sent to {recipient}"
    def get_service(self):
        return f'Сервис: {self._service}'
class PushSender(NotificationSender):
    def __init__(self, service = "Firebase"):
        self._service = service
    def send(self, message, recipient):
        return f"Push sent to {recipient}"
    def get_service(self):
        return f'Сервис: {self._service}'
email = EmailSender()

class UserAuth:
   def __init__(self, username, account: BankAccount, notifier: NotificationSender):
       self.username = username
       self.account = account
       self.notifier = notifier
   def login(self,password):
       result = self.account.get_balance(password)
       if result != "Неверный пароль!":
           print(self.notifier.send(f"Успешный вход: {self.username}", "john@mail.ru"))
           return True
       else:
           print("Неверный пароль!")
           return False
   def transfer(self, amount, password, recipient_account: BankAccount):
         balance_check = self.account.get_balance(password)
         if balance_check != "Неверный пароль!":
             print(self.account.get_balance(password))
             return True
         result = self.account.withdraw(amount, password)
         if result == "Неверный пароль!" or result == "Недостаточно средств!":
             print("Ошибка перевода", result)
             return False
         print(self.notifier.send(f"Перевод {amount} отправлен", "отправитель"))
         print(self.notifier.send(f"Получено {amount} от {self.username}", "получатель"))

         recipient_account._balance += amount

john = BankAccount("John", 100, "123qwerty")
notifier = EmailSender()
john = UserAuth("John",  john, notifier)
print(john.account.deposit(50, "123qwerty"))
print(john.account.withdraw(200, "123qwerty"))
print(john.account.get_balance("123qwerty"))
print(john.account.change_password("wrong", "new"))
print(john.account.reset_pin("123qwerty"))
print(email.send("Привет", "john@mail.ru"))
print(email.get_service())
print(john.login("123qwerty"))


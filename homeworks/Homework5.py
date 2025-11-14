class User:
   def __init__(self, name, is_admin=False):
       self.name = name
       self.is_admin = is_admin

def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if user.is_admin:
            return func(user, *args, **kwargs)
        else:
             print(f"PermissionError: Доступ запрещён! Только админ может выполнить эту операцию.")
    return wrapper

@admin_only
def delete_database(user):
   print("База данных удалена!")

admin = User("Алексей", is_admin=True)
user = User("Мария", is_admin=False)
delete_database(admin)
delete_database(user)







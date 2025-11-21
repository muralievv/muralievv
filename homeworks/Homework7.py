import sqlite3
connect = sqlite3.connect("boxers.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS boxers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL,
    record TEXT NOT NULL
     )
''')
connect.commit()
def create_user(name, age, record):
    cursor.execute(
        'INSERT INTO boxers(name, age, record) VALUES(?,?,?)',
        (name,age,record)
    )
    connect.commit()
    print("боксер добавлен")
#create_user("Mike_Tyson", 59, "50-7")
def read_boxers():
    cursor.execute('SELECT name, age, record FROM boxers')
    boxers = cursor.fetchall()
    print(boxers)
def detail_boxer(id):
    cursor.execute(
'SELECT name, age, record from boxers WHERE id = ?',
        (id,)
)
    boxer = cursor.fetchone()
    print(boxer)



def update_boxer(name, age, record, id):
    cursor.execute(
        'UPDATE boxers SET name = ?, age = ?, record = ? WHERE id = ?',
        (name, age, record, id)
    )
    connect.commit()
    print(f'Боксер с id{id} обновлен')


def delete_boxer(id):
    cursor.execute('DELETE FROM boxers WHERE id = ?',
                   (id,))
    connect.commit()
    print(f'Боксер с id {id} удален')
read_boxers()
detail_boxer(2)
update_boxer("Muhammad_Ali", 65, "56-5", 4)
delete_boxer(4)
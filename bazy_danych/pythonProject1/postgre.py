import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# tabela studenci
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# tabela kursy
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_name TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
''')

def dodaj_studenta(name):
    try:
        cursor.execute('INSERT INTO students (name) VALUES (?)', (name,))
        conn.commit()
        print('Dodano nowego studenta:', name)
    except Exception as e:
        print('Błąd podczas dodawania studenta:', e)


def dodaj_kurs(student_id, course_name):
    try:
        cursor.execute('INSERT INTO courses (student_id, course_name) VALUES (?, ?)', (student_id, course_name))
        conn.commit()
        print('Dodano nowy kurs:', course_name)
    except Exception as e:
        print('Błąd podczas dodawania kursu:', e)



dodaj_studenta('Jan Nowak')
dodaj_kurs(1, 'Fizyka')


conn.close()

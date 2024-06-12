const sqlite3 = require('sqlite3').verbose();

// Konfiguracja połączenia z bazą danych SQLite
const db = new sqlite3.Database(':memory:');

// Tworzenie tabeli students
db.run(`
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
`);

// Tworzenie tabeli courses
db.run(`
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_name TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
`);

// Dodawanie nowego rekordu do tabeli students
const dodajStudenta = async (name) => {
    try {
        await db.run('INSERT INTO students (name) VALUES (?)', [name]);
        console.log('Dodano nowego studenta:', name);
    } catch (err) {
        console.error('Błąd podczas dodawania studenta:', err);
    }
};

// Dodawanie nowego rekordu do tabeli courses
const dodajKurs = async (student_id, course_name) => {
    try {
        await db.run('INSERT INTO courses (student_id, course_name) VALUES (?, ?)', [student_id, course_name]);
        console.log('Dodano nowy kurs:', course_name);
    } catch (err) {
        console.error('Błąd podczas dodawania kursu:', err);
    }
};

// Wywołanie funkcji dodających rekordy
(async () => {
    await dodajStudenta('Jan Nowak');
    await dodajKurs(1, 'Fizyka');
})();

// Zamknięcie połączenia z bazą danych po zakończeniu operacji
db.close((err) => {
    if (err) {
        console.error('Błąd podczas zamykania połączenia z bazą danych:', err.message);
    } else {
        console.log('Połączenie z bazą danych zamknięte.');
    }
});

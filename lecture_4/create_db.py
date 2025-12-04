import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS grades')
cursor.execute('DROP TABLE IF EXISTS students')

cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_year INTEGER
)
''')

cursor.execute('''
CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
''')

students_data = [
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006)
]

cursor.executemany('INSERT INTO students (full_name, birth_year) VALUES (?, ?)', students_data)

grades_data = [
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94)
]

cursor.executemany('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', grades_data)

conn.commit()
conn.close()

print("База данных успешно создана!")
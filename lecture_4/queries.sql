
-- 3. Все оценки для Brian Smith
SELECT s.full_name, g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Brian Smith';

-- 4. Средняя оценка по каждому студенту
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC;

-- 5. Студенты, родившиеся после 2004 года
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 6. Средняя оценка по каждому предмету
SELECT subject, ROUND(AVG(grade), 2) AS avg_grade
FROM grades
GROUP BY subject
ORDER BY avg_grade DESC;

-- 7. Топ-3 студента по средней оценке
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC
LIMIT 3;

-- 8. Студенты, у которых есть хотя бы одна оценка ниже 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;

CREATE INDEX idx_students_name ON students(full_name);

CREATE INDEX idx_grades_student ON grades(student_id);
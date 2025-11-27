# Student Grade Analyzer

A simple Python console program for accounting and analyzing student performance

## Opportunities

- Adding a new student
- Entering grades (from 0 to 100) for the selected student
- Generating a report with the average scores of each student
- General statistics output:
   - maximum and minimum average score
   - average score for the group
   - number of students and students with grades
- Determination of the student with the highest average score (and if there are ≥ 3 students with grades, the top 3)

## Requirements

- Python 3.6 or higher
- Python Standard Library (no external dependencies)

## Running
```bash
uv run main.py
```

## Implementation features

- Student search is case insensitive
- All input errors are handled with the output of clear messages
- The data is stored as a dictionary list
- The program is resistant to incorrect input and interruption

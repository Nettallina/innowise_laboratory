"""The student Grade Analyzer"""

def add_students(students):
    """
    Add a new student to the list. 
    :param students: list of dictionaries.
    """
    try:
        name = input("Enter student name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty")      
        students_exists = any(map(lambda s: s["name"].lower() == name.lower(), students))

        if students_exists:
            print(f"Student '{name}' already exists")
            return 
        new_student = {
            "name": name,
            "grades": []
        }
        students.append(new_student)
        print(f"Student '{name}' added successfully")
    
    except ValueError as ve:
        print(f"Errror: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def add_grades(students):
    """
    Add grades for existing student.
    :param students: list of dictionaries.
    """
    try:
        if not students:
            print("No students available, please add one more")
            return
        
        name = input("Enter student name: ").strip()

        
        student = None
        student_index = None

        for i, s in enumerate(students):
            if s["name"].lower() == name.lower():
                student_index = i
                student = s
                break
        
        if student is None:
            raise IndexError(f"Student '{name}' not found")
        
        print(f"Adding grades for {student['name']}: ")
        print("Type 'done' to finish adding")

        grades = 0
        while True:
            try:
                grade = input("Enter a grade or 'done' to finish: ").strip().lower()

                if grade == 'done':
                    break

                valid_grade = lambda x: 0 <= float(x) <= 100

                if not valid_grade(grade):
                    raise ValueError("Grade must be between 0 and 100")
                
                grade = float(grade)
                student["grades"].append(grade)
                grades += 1
                print(f"Grade {grade} added successfully")

            except ValueError as ve:
                print(f"Invalid input {ve}. Please enter a number")
            except Exception as e:
                print(f"Error adding grade: {e}")
        print(f"Successfully adde {grades} grades for {student['name']}")
    
    except IndexError as ie:
        print(f"Error: {ie}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def calculate_average(grades):
    """
    Calculate average ages for students
    :param grades: the list of grades for each student.
    """

    try:
        if not grades:
            return None
        
        safe_sum = lambda g_list: sum(g_list) if g_list else 0
        total = safe_sum(grades)

        return total / len(grades)
    
    except ZeroDivisionError:
        print("Error: zero division")
        return None
    except Exception as e:
        print(f"Error calculating average: {e}")
        return None

def show_report(students):
    """
    Show the full report for each student.
    :param students: list of dictionaries.
    """
    try:
        if not students:
            print("No student available")
            return      
        print("-*-*-Student report-*-*-")

        averages = []
        valid_averages = []

        for i, student in enumerate(students, 1):
            try:
                avg = calculate_average(student["grades"])

                if avg is not None:
                    averages.append(avg)
                    valid_averages.append(avg)
                    print(f"{i}. {student['name']}'s average grade is {avg:.1f}")
                else:
                    averages.append(None)
                    print(f"{i}. {student['name']}'s average grade is N/A")
            except Exception as e:
                print(f"{i}. {student['name']}: Error calculating average - {e}")
                averages.append(None)

        if valid_averages:
            get_max = lambda arr: max(arr) if arr else 0
            get_min = lambda arr: min(arr) if arr else 0
            get_overall_avg = lambda arr: sum(arr) / len(arr) if arr else 0

            max_avg = get_max(valid_averages)
            min_avg = get_min(valid_averages)
            overall_avg = get_overall_avg(valid_averages)

            print("-*-*-*-")
            print(f"Max Average: {max_avg:.1f}")
            print(f"Min Average: {min_avg:.1f}")
            print(f"Overall Average: {overall_avg:.1f}")
            print(f"Total Students: {len(students)}")
            print(f"Students with Grades: {len(valid_averages)}")
        else:
            print("-*-*-*-")
            print("No grades available for statistics.")

    except Exception as e:
        print(f"Error generation report: {e}")

def find_top(students):
    """
    Find student with max grade average.
    :param students: list of dictionaries.
    """
    try:
        if not students:
            print("No students available")
            return
        students_with_grades = list(filter(lambda s: s["grades"], students))

        if not students_with_grades:
            print("No students with grades available")
            return       
        top_student = max(students_with_grades,
                          key=lambda s: sum(s["grades"]) / len(s["grades"]))      
        top_avg = calculate_average(top_student["grades"])

        top_index = None
        for i, student in enumerate(students):
            if student["name"] == top_student["name"]:
                top_index = i + 1
                break       
        print(f"The student with the highest average is {top_student['name']} "
              f"(#{top_index}) with a grade of {top_avg:.1f}.")       
        if len(students_with_grades) >= 3:
            try:
                sorted_students = sorted(students_with_grades, 
                                       key=lambda s: sum(s["grades"]) / len(s["grades"]), 
                                       reverse=True)               
                print("Top 3 performers:")
                for i, student in enumerate(sorted_students[:3], 1):
                    avg = calculate_average(student["grades"])
                    print(f"  {i}. {student['name']}: {avg:.1f}")
            except Exception as e:
                print(f"Note: Could not display top 3 ranking: {e}")   
    except ValueError as ve:
        print(f"Error finding top performer: {ve}")
    except Exception as e:
        print(f"Unexpected error while finding top performer: {e}")

def main():
    """
    Main function for managing and analyzing students grades.
    It uses the list of dictionaries for storing students data.
    """
    students = []

    while True:
        print("-*-*-Student Grade Analyzer-*-*-")
        print("1. Add a new student")
        print("2. Add grades for students")
        print("3. Show report for all students")
        print("4. Find top")
        print("5. Exit")

        try:
            choice = input("Enter the option: ").strip()

            if choice == "1":
                add_students(students)
            elif choice == "2":
                add_grades(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top(students)
            elif choice == "5":
                print("Bye")
                break
            else:
                raise ValueError("Invalid operation")
                
        except Exception as e:
            print(f"An unexpected error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program was interrupted")

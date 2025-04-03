def student_grades_tracker(students):
    dict = {name: grades for name, grades in students}

    def avg(grades):
        return sum(grades) / len(grades) if grades else 0
    
    average_grades = {name: avg(grades) for name, grades in dict.items()}

    highest_avg_student = max(average_grades, key = average_grades.get)
    
    passed_students = sum(1 for avg in average_grades.values() if avg >= 50)

    return dict, average_grades, highest_avg_student, passed_students

students = [
    ("swagath",[55,66,77,88,99]),
    ("Goutham",[68,76,56,44,90]),
    ("Asha",[82,64,73,73,88]),
    ("pravalika",[45,54,61,62,63]),
]

dict, average_grades, highest_avg_student, passed_students = student_grades_tracker(students)
 
print(" students and their grades: ")
print(dict)
print("\n average of grades:")
print(average_grades)
print("\n student with highest average: ")
print(highest_avg_student)
print("\n passed students:")
print(passed_students)

    
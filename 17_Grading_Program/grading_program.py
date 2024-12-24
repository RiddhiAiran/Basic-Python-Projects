student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for keys in student_scores:
    if 91 < student_scores[keys] <= 100:
        student_grades[keys] = 'Outstanding'
    elif 81 < student_scores[keys] < 90:
        student_grades[keys] = 'Exceeds Expectations'
    elif 71 < student_scores[keys] < 80:
        student_grades[keys] = 'Acceptable'
    elif student_scores[keys] <= 70:
        student_grades[keys] = 'Fail'
print(student_grades)
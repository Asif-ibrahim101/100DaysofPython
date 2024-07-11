student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    
    if score > 90:
        student_scores[student] = "outstanding"
    elif score > 80:
        student_scores[student] = "Exceeds Expectations"
    elif score > 70:
        student_scores[student] = "Acceptable"
    elif score == 70 or score < 70:
        student_scores[student] = "Fali"
    else:
        print("you did something wrong")
        
student_grades.update(student_scores)
print(student_grades)
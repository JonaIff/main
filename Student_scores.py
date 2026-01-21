student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={
    
}

for key in student_scores:
    
    grade = student_scores[key] 
    if grade <= 70:
        grading = "Fail"
        
    if grade >= 71 and grade <= 80:
        grading = "Acceptable"
    
    if grade >= 81 and grade <= 90:
        grading = "Exceeds Expectations"
    if grade >= 91 and grade <= 100:
        grading = "Outstanding"
        
    student_grades[key] = grading
    print(key)
    
print(student_grades)
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    

def is_passing(grade):
    if grade == 'A':
        return True
    elif grade == 'B':    
        return True
    elif grade == 'C':    
        return True
    
    return False
    

def is_honors(grade, score):
    if score >= 95:
        return True
    
    return False

score1 = 85
grade1 = calculate_grade(score1)
print(f"Score: {score1}, Grade: {grade1}, Passing: {is_passing(grade1)}, Honors: {is_honors(grade1, score1)}") 

score2 = 96
grade2 = calculate_grade(score2)
print(f"Score: {score2}, Grade: {grade2}, Passing: {is_passing(grade2)}, Honors: {is_honors(grade2, score2)}")

score3 = 58
grade3 = calculate_grade(score3)
print(f"Score: {score3}, Grade: {grade3}, Passing: {is_passing(grade3)}, Honors: {is_honors(grade3, score3)}")



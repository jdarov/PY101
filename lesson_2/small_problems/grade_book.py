GRADES = {
    'A': range(90, 101),
    'B': range(80, 90),
    'C': range(70, 80),
    'D': range(60, 70),
    'F': range(0, 60)
    }

def get_grade(score1, score2, score3):
    average = int((score1+score2+score3)/3)
    for grade, scores in GRADES.items():
        if average in scores:
            return grade

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
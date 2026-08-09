def check_score(Scores):
    for i in range(5):
        if Scores[i] >= 50:
            print(f"Student {i+1} | score {Scores[i]} : Pass.")
        else:
            print(f"Student {i+1} | score {Scores[i]} : Not pass.")
            
print("-"*30)            
print("         Exam Score")
print("-"*30)
print()
  
Scores = []
for i in range(5):
    score = int(input(f"Enter score of student {i+1} : "))
    Scores.append(score)

check_score(Scores)
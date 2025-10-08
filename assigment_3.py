#assigment_3.py
def sum_score (scores) :
    if not scores: 
       return 0
    return scores[0] + sum_score(scores[1:])


students = []


n = int(input("enter number of students :"))

for i in range (n) :

 name = input(f"enter the name for student {i+1} :")
 score = float(input(f"enter the score for {name} :"))
 students.append((name,score))

  

print("\nall students (name , score ):")
for name , score in students :
   print (f"{name}, {score}")


scores = [ score for _, score in students]
aver = sum_score(scores)/len(scores)
top_student = max(students , key =lambda s : s[1])
failed= [name for name,score in students if score <60]

print (f"average score : {aver}")
print (f"top students : {top_student[0]} , {top_student[1]}")

if not failed :
 print("No students failed!")
else:
  print("Failed students:")
for f in failed :
 print("-",f)


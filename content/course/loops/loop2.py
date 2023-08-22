student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

largests_score = student_scores[0]

for number in student_scores:
    if number > largests_score:
        largests_score = number

print("The highest score in the class is: {}".format(largests_score))
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
for i, a in enumerate(student_heights):
    total_height += a

element = 0
for x in student_heights:
    element += 1

avarage_height = total_height / element

print(round(avarage_height))
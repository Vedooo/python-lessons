import random as rd

# LIST COMPRE

# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Vedo"
# new_list = [letter for letter in name]
# print(new_list)


# new_list = [n * 2 for n in range(1,5)]
# print(new_list)


# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# new_list = [name for name in names if len(name) < 5]
# print(new_list)

# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)

# numbers = [1,1,2,3,5,8,13,21,34,55]

# square_nums = [n * n for n in numbers]
# print(square_nums)

# even_nums = [n for n in numbers if n % 2 == 0]
# print(even_nums)


# DICT COMPHRE

# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

# student_scores = {name: rd.randint(1,100) for name in names}
# print(student_scores)

# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the airspeed velocity of an unladen swallow"

# result = {word: len(word) for word in sentence.split()}
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 16,
#     "Friday": 20,
#     "Saturday": 19,
#     "Sunday": 21,
# }

# fahrenait = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}
# print(fahrenait)
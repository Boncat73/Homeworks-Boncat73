# Task 1: створювання словника, доступ до елементів та друк
#створюємо словник
my_dict = {
    "name": "Vasyl", 
    "age": 52,
    "course_1": "English",
    "course_2": "Python Backend Development"
}

#доступ до елементів
my_dict_name = my_dict["name"]
my_dict_age = my_dict["age"]
my_dict_course_1 = my_dict["course_1"]
my_dict_course_2 = my_dict["course_2"]

#виведення
print("Task 1:")
print("Person 1:")
print(f"Name first person: {my_dict_name}.")
print(f"Age this person: {my_dict_age}.")
print(f"This person learn: {my_dict_course_1} and {my_dict_course_2}.")

print(" ")

# Task 2: створювання кількох елементів, доступ до них та друк
# створюємо словник
student_info = {
    "name_1": "Daniel",
    "age_1": 23,
    "course_1": "Animation",
    "name_2": "George",
    "age_2": 21,
    "course_2": "English",
    "name_3": "Vasyl",
    "age_3": 52,
    "course_1_3": "English",
    "course_2_3": "Python and Backend Development"
}

#доступ до елементів
student_info_name_1 = student_info["name_1"]
student_info_age_1 = student_info["age_1"]
student_info_course_1 = student_info["course_1"]

student_info_name_2 = student_info["name_2"]
student_info_age_2 = student_info["age_2"]
student_info_course_2 = student_info["course_2"]
                                     
student_info_name_3 = student_info["name_3"]
student_info_age_3 = student_info["age_3"]
student_info_course_1_3 = student_info["course_1_3"]
student_info_course_2_3 = student_info["course_2_3"]

#виведення
print("Task 2:")
print(f"First person: {student_info_name_1}, {student_info_age_1}, {student_info_course_1}.")
print(f"Second person: {student_info_name_2}, {student_info_age_2}, {student_info_course_2}.")
print(f"Third person: {student_info_name_3}, {student_info_age_3}, {student_info_course_1_3}, {student_info_course_2_3}.")

#Dictionaries

# syntax: {key:value}
# programming_dictionary ={
#      "Bug":"An error in a program that prevents the program from running as expected",
#      "Function":"A piece of code that you can easily call over and over again"
#  }
# print(programming_dictionary["Bug"])
# programming_dictionary["loop"]="The action of doing something over and over again."
# print(programming_dictionary)

# empty_dictionary={}
# empty_dictionary[1]=one

# # Wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"]="A moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# code challenge:
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades ={}
# for scores in student_scores:
#     student_grades[scores]=student_scores[scores]
#     if student_grades[scores] >= 91:
#         student_grades[scores]="Outstanding"
#     elif 81 <= student_grades[scores] <= 90:
#         student_grades[scores] = "Exceeds Expectations"
#     elif 71 <= student_grades[scores] <= 80:
#         student_grades[scores] = "Acceptable"
#     elif student_grades[scores] <= 70:
#         student_grades[scores] = "Fail"
# print(student_grades)

# Nested dictionary
# {key:[list],key2:{dict}}
#
# # capitals={"France":"Paris","Germany":"Berlin"}

# Nested list in dictionary
# travel_log={"France":["Paris","Lille","Nice"],"Germany":["Stuttgart","Berlin"]}
# print(travel_log["France"][1])

# nested_list=["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log={"France":{"cities_visited":["Paris","Lille","Nice"],"Total_visits":12},"Germany":{"cities_visited":["Stuttgart","Berlin","Hamburg"],"Total_visits":5}}
print(travel_log["Germany"]["cities_visited"][0])
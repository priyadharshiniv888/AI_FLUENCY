import json

print("Rule-Based Workflow")

with open("student_data.json", "r") as file:
    data = json.load(file)

marks = data["marks"]

highest_subject = max(marks, key=marks.get)
highest_mark = marks[highest_subject]

print("Highest mark subject:", highest_subject)
print("Highest mark:", highest_mark)
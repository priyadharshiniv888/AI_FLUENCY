import json

def get_student_marks():
    with open("student_data.json", "r") as file:
        data = json.load(file)

    return data["marks"]
def get_distance(place1, place2):
    distances = {
        ("Chennai", "Coimbatore"): 510,
        ("Coimbatore", "Chennai"): 510
    }

    return distances.get((place1, place2), "Distance not available")


def calculate_total_budget(students, budget_per_student):
    return students * budget_per_student
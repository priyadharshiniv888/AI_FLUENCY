from tools import get_distance, calculate_total_budget


def react_agent():
    print("REACT AGENT")
    print("-----------")

    question = "Three students are travelling from Chennai to Coimbatore. Each student has Rs.1500. Find the distance and total budget."

    print("Question:", question)

    print("\nThought: I need the distance between Chennai and Coimbatore.")
    
    print("Action: Calling distance tool...")
    distance = get_distance("Chennai", "Coimbatore")

    print("Observation:", distance, "km")

    print("\nThought: Now I need to calculate the total budget.")
    
    print("Action: Calling budget tool...")
    budget = calculate_total_budget(3, 1500)

    print("Observation: Rs.", budget)

    print("\nFinal Answer:")
    print("Distance:", distance, "km")
    print("Total Budget: Rs.", budget)


react_agent()
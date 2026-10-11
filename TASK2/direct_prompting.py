def direct_prompt(question):
    print("DIRECT PROMPTING")
    print("----------------")
    print("Question:", question)

    answer = (
        "For a 3-student trip with a budget of Rs.1500 per student, "
        "the total budget is Rs.4500."
    )

    print("Answer:", answer)


question = "Three students have Rs.1500 each. What is their total trip budget?"

direct_prompt(question)
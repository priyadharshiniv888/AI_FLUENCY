import random

question = "Three students have Rs.1500 each. What is their total trip budget?"

answers = []

for i in range(5):
    possible_answers = [4500, 4500, 4500, 4500, 3000]
    answer = random.choice(possible_answers)
    answers.append(answer)
    print("Run", i + 1, ":", answer)

print("\nQuestion:", question)

majority_answer = max(set(answers), key=answers.count)

print("Majority Answer:", majority_answer)
print("Correct Answer: 4500")

if majority_answer == 4500:
    print("Majority answer is CORRECT")
else:
    print("Majority answer is WRONG")
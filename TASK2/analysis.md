# Day 2 Task – Reasoning and Acting

## Scenario

The scenario chosen for this task is a student trip from Chennai to Coimbatore.

The problem contains questions that require reasoning and a question that requires external information through a tool. Three students have a budget of Rs.1500 each. The task is to find their total budget and the distance between Chennai and Coimbatore.

The same scenario is demonstrated using Direct Prompting, Chain-of-Thought, and a ReAct agent.

---

## 1. Direct Prompting

Direct prompting gives an answer directly to the user's question without showing intermediate reasoning.

In this scenario, the question was:

"Three students have Rs.1500 each. What is their total trip budget?"

The direct prompting program immediately produced the answer Rs.4500.

Direct prompting does not use any external tool. It depends on the information and reasoning available to the model. It is suitable for simple questions where no external information is required.

However, it has limitations when a question requires information that is not already available to the model. In this scenario, direct prompting cannot independently obtain the Chennai-to-Coimbatore distance using a tool.

---

## 2. Chain-of-Thought

Chain-of-Thought prompting breaks a problem into multiple reasoning steps before producing the final answer.

For the budget question, the reasoning was demonstrated as:

1. Identify the number of students.
2. Identify the budget per student.
3. Multiply the number of students by the budget per student.
4. Produce the final answer.

The final answer was Rs.4500.

Chain-of-Thought improves the handling of multi-step reasoning questions because the problem is divided into smaller steps. However, it does not automatically provide external facts that are not available to the model.

In this scenario, Chain-of-Thought can reason about the budget calculation, but it cannot independently obtain the distance using an external tool.

---

## 3. ReAct Agent

ReAct combines reasoning with actions and observations. It can decide that external information is required, call a tool, observe the result, and continue reasoning.

The ReAct agent followed this cycle:

Thought:
I need the distance between Chennai and Coimbatore.

Action:
Calling the distance tool.

Observation:
510 km.

Thought:
Now I need to calculate the total budget.

Action:
Calling the budget tool.

Observation:
Rs.4500.

Final Answer:
Distance: 510 km  
Total Budget: Rs.4500

This demonstrates the Thought, Action, and Observation cycle.

The ReAct agent is useful for this scenario because the problem requires both reasoning and external information from tools.

---

## 4. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Low for multi-step problems | Higher because the problem is divided into steps | Higher because reasoning and tool actions are combined |
| Tool usage | No tool usage | No tool usage in this task | Uses tools when external information is required |
| Reliability on multi-step questions | Can be less suitable for complex multi-step tasks | Can improve multi-step reasoning | Can handle multi-step tasks involving tools |
| Transparency | Gives a direct answer without visible reasoning | Shows reasoning steps in this demonstration | Shows Thought, Action and Observation in this demonstration |
| Speed / cost | Fast and simple | More reasoning steps may require more processing | Tool calls add extra steps and processing |
| Consistency across repeated runs | Generally simple and direct | Can vary when model sampling is non-zero | Can vary depending on reasoning and tool results |

---

## 5. Self-Consistency Observation

The budget question was run multiple times using the self-consistency demonstration script.

The five observed answers were:

- Run 1: 4500
- Run 2: 4500
- Run 3: 4500
- Run 4: 4500
- Run 5: 3000

The majority answer was 4500.

The correct answer is 4500 because:

3 students × Rs.1500 = Rs.4500

Therefore, the majority answer was correct.

The demonstration script uses random selection to simulate answer variation. It is not an actual LLM temperature experiment. In an actual model-based experiment, a non-zero temperature can allow different sampled answers, while temperature 0 is intended to make generation more deterministic.

---

## 6. Suitability Analysis

For this particular scenario, the ReAct approach is suitable because the problem requires both reasoning and external information.

Direct prompting can quickly solve the simple budget calculation, but it does not use a tool to obtain the distance.

Chain-of-Thought can break the budget problem into reasoning steps, but it also does not independently obtain external information.

The ReAct approach can combine reasoning with tool usage. It first identifies that the distance is required, calls the distance tool, observes the result, and then uses another tool to calculate the total budget.

The self-consistency experiment also showed that repeated reasoning outputs can sometimes vary. In the demonstration, four out of five runs produced the correct majority answer of 4500.

---

## 7. Conclusion

Direct prompting is appropriate for simple questions where the required information is already available and a quick answer is needed.

Chain-of-Thought is useful for problems that require multiple reasoning steps. It can help break a complex problem into smaller steps, but it does not automatically provide missing external information.

ReAct is appropriate for problems that require both reasoning and interaction with external tools. It follows a cycle of Thought, Action, and Observation and can use information returned by tools before producing the final answer.

Therefore, the choice of approach depends on the type of problem. Simple questions can use direct prompting, multi-step reasoning questions can use Chain-of-Thought, and tasks requiring external information or tools can use ReAct.
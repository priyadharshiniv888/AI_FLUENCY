# Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario

The chosen private-data scenario is a student's academic marks. The student data is stored in a private JSON file named `student_data.json`. The file contains the student's name and marks in Python, Java, and AI.

The user's request is:

"Which is my highest mark?"

The same request is handled using a plain chatbot, a rule-based workflow, and an AI agent.

## 2. Plain Chatbot

The plain chatbot uses an LLM to generate a response. It does not have access to the private `student_data.json` file and does not use any tools.

When the user asks which mark is the highest, the chatbot explains that it does not have access to the student's private academic records.

The main limitation is private-data access. Without a tool or data-access mechanism, the chatbot cannot read the student's actual marks and determine the highest mark from the private file.

## 3. Rule-Based Workflow

The rule-based workflow uses predefined program logic and does not use an LLM.

It reads the `student_data.json` file, obtains the subject marks, and uses a predefined rule to find the subject with the highest mark.

For this scenario, the workflow identifies AI as the subject with the highest mark, with a score of 92.

Its limitation is flexibility. The workflow follows the rules written by the programmer and is designed for the specific predefined task.

## 4. AI Agent

The AI agent combines an LLM, a tool, and a loop.

The LLM receives the user's question and decides that it needs the student's private marks. It then uses the `get_student_marks` tool.

The tool reads the private `student_data.json` file and returns the subject marks to the agent.

The agent observes the tool result and generates the final answer. The implementation also uses a loop so the user can ask multiple questions until they type `exit`.

For the request "Which is my highest mark?", the agent uses the private-data tool and returns that the highest mark is 92 in AI.

## 5. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Handles general conversation | Depends on predefined rules | Can combine LLM reasoning with tools |
| Decision-making | Generates responses using the LLM | Uses predefined conditions and logic | LLM can decide when a tool is needed |
| Tool usage | No tool used | Uses program logic to read data | Uses a tool to access private data |
| Private-data access | Not available in our implementation | Directly reads the JSON file | Accesses the JSON file through a tool |
| Multi-step task handling | Limited in this scenario | Follows predefined steps | Can use a tool, observe its result, and continue |
| Automation | Limited | High for predefined tasks | Can automate tasks involving tools and multiple steps |
| Reliability | Depends on the generated response | Consistent for the programmed rule | Depends on LLM reasoning and tool execution |

## 6. Suitability Analysis

The plain chatbot is suitable when the user needs a general conversational response and private-data access is not required.

The rule-based workflow is suitable when the task is clearly defined and the required steps and conditions are known in advance.

The AI agent is suitable when the task requires an LLM to work with private data through tools and may involve multiple steps. In this scenario, the agent uses the student-marks tool, observes the returned data, and produces the requested result.

## 7. Conclusion

A plain chatbot is appropriate for general conversational questions where external tools or private data are not required.

A rule-based workflow is appropriate for predictable tasks where the steps and conditions can be predefined.

An AI agent is appropriate for tasks that require an LLM to work with tools, observe results, and continue through multiple steps until the task is completed.

The three approaches demonstrate different levels of flexibility, private-data access, decision-making, tool usage, and automation.
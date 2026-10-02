import json
from config import client, MODEL
from tools import get_student_marks


def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": (
                "You are a student marks assistant. "
                "Private student marks are available only through the "
                "get_student_marks tool. "
                "Use the tool when the user asks about their marks. "
                "Do not invent marks."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    while True:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_student_marks",
                        "description": "Get the student's private subject marks.",
                        "parameters": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                }
            ],
            tool_choice="auto"
        )

        message = response.choices[0].message

        if message.tool_calls:

            messages.append(message)

            for tool_call in message.tool_calls:

                if tool_call.function.name == "get_student_marks":

                    marks = get_student_marks()

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps(marks)
                        }
                    )

        else:
            return message.content


print("AI Agent")

while True:

    question = input("\nAsk something (type exit to stop): ")

    if question.lower() == "exit":
        print("Agent stopped.")
        break

    answer = run_agent(question)

    print("Agent:", answer)
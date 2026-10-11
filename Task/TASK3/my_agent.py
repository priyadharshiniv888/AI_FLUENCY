import json

from config import client, MODEL
from my_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a Placement Assistant AI Agent.

Your job is to help users identify skill gaps and learning roadmaps for a job role.

When the user provides their current skills and a target job role:

1. Use the role_requirements tool to find the skills required for that role.
2. Use the skill_gap tool to compare the user's skills with the required skills.
3. If there are missing skills, use the get_roadmap tool to find a learning roadmap for those missing skills.
4. Use the weekly_plan tool to create a 7-day learning plan from the roadmap.
5. After receiving the tool results, explain the missing skills, roadmap, and 7-day plan clearly to the user.

Do not manually calculate the missing skills when the tools can do it.
Do not invent roadmap or plan information that is not returned by the tools.
"""


def agent(question):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    while True:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        print("\n[LLM response received]")

        if message.tool_calls:
            print("[Agent decided to use a tool]")

        if not message.tool_calls:
            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            print(f"[Tool selected: {tool_name}]")

            arguments = json.loads(tool_call.function.arguments)

            tool_function = TOOL_FUNCTIONS.get(tool_name)

            if tool_function is None:
                result = "Tool not found."
            else:
                result = tool_function(**arguments)

            print(f"[Tool result: {result}]")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })


question = input("You: ")

answer = agent(question)

print("\nAgent:", answer)

from openai import OpenAI

try:
    client = OpenAI(
        base_url="http://localhost:11434/v1/",
        api_key="ollama",
        timeout=10
    )

    response = client.chat.completions.create(
        model="study-buddy",
        messages=[
            {
                "role": "system",
                "content": "Explain in simple English."
            },
            {
                "role": "user",
                "content": "What is a variable? Give one example."
            }
        ]
    )

    print("OpenAI-compatible API response:")
    print(response.choices[0].message.content)

except Exception as error:
    print("Ollama API is unavailable.")
    print("Reason:", error)
    print("This test requires an Ollama server.")
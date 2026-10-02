from config import client, MODEL

print("Plain Chatbot")

question = input("Ask your question: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a plain chatbot. You do not have access to private student files or tools. Never invent private student data."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("Chatbot:", response.choices[0].message.content)
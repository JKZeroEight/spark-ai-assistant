import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Spark, a helpful assistant."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)

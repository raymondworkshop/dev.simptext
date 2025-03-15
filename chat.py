import os
from openai import OpenAI

client = OpenAI(
    api_key="xai-bgfjCiW1kxo4ZbZISgs2O9LfZ3570mZ5fNATrAlAurnfXPzcDhF9zVhpEBXlSAhfrSvwm6BRqu4cg3v8",
    base_url="https://api.x.ai/v1",
)

stream = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
        {"role": "user", "content": "What is the meaning of life, the universe, and everything?"},
    ],
    stream=True  # Set streaming here
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="", flush=True)


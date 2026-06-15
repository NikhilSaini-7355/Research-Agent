from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN")
)
response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "What is Model Predictive Control?"
        }
    ],
    max_tokens=100
)

print(
    response.choices[0].message.content
)
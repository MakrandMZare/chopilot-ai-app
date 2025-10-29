"""Run this model in Python

> pip install openai
"""

import os
from openai import OpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"],
    default_query={
        "api-version": "2024-08-01-preview",
    },
)

messages = []

tools = []

response_format = {"type": "text"}

while True:
    response = client.chat.completions.create(
        messages=messages,
        model="openai/gpt-4.1",
        tools=tools,
        response_format=response_format,
        temperature=1,
        top_p=1,
    )

    if response.choices[0].message.tool_calls:
        print(response.choices[0].message.tool_calls)
        messages.append(response.choices[0].message)
        for tool_call in response.choices[0].message.tool_calls:
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": [
                        {
                            "type": "text",
                            "text": locals()[tool_call.function.name](),
                        },
                    ],
                }
            )
    else:
        print("[Model Response] " + response.choices[0].message.content)
        break

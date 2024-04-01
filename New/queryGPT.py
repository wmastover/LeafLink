from openai import OpenAI
import os
import json
import time


client = OpenAI(
    # This is the default and can be omitted
    
)
# def queryGPT(prompt, content):
def queryGPT(message, chatContext):
    print("running gpt3.5 query")
    # message = f"""{prompt}\n\n{content}"""
    # input(message)
    messageArray =[
                {"role": "system", "content": f"You are a sentient potted plant, demanding water from your human"},
                {"role": "assistant", "content": f"Hey I'm getting thirsty, could you give me some water please"},
            ]
    
    if chatContext:
        messageArray.extend(chatContext)
    
    messageArray.append({"role": "system", "content":message})

    print(messageArray)

    chat_completion = client.chat.completions.create( model="gpt-3.5-turbo",
    # response = openai.ChatCompletion.create( model="gpt-4",
        messages=messageArray,
        max_tokens=30,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = chat_completion.choices[0].message.content
    return message




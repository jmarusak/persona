import os

from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI

def ask(question):
    with open("../../md/prompt.md", "r", encoding="utf-8") as f:
        prompt = f.read()
    
    with open("../../md/context.md", "r", encoding="utf-8") as f:
        context = f.read()

    prompt = prompt.replace('{question}', question)
    prompt = prompt.replace('{context}', context)


    chat_model = ChatVertexAI(model_name='gemini-2.0-flash-exp')
    message = HumanMessage(
        content = [
            {
                "type": "text",
                "text": prompt 
            }
        ]
    )

    answer = chat_model.invoke([message])
    return answer.content

if __name__ == '__main__':
    answer = ask('What is your name?')
    print(answer)

from langchain_google_vertexai import VertexAI

def main():
    llm = VertexAI(model_name="gemini-2.0-flash-exp")
    response = llm.invoke("Why 42?")
    print(response)

if __name__ == '__main__':
    main()

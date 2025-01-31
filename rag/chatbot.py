import streamlit as st

from model import ask

def main():
    st.title("Chatbot")

    question = st.text_input("Question:")

    answer = ""
    if st.button("Submit"):
        answer = ask(question) 
    
    st.text_area("Answer:", answer, height=200)

if __name__ == "__main__":
    main()

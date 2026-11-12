"""Week 10: College Assistant chatbot using LangChain and Ollama."""

import csv
from pathlib import Path

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "dataset"
MODEL_NAME = "llama3.2"

# Reusable prompt template with placeholders.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful college assistant. Answer clearly and simply. "
               "If you do not know an official college-specific detail, say so."),
    ("human", "Category: {category}\nStudent question: {question}")
])

def main():
    print("COLLEGE ASSISTANT CHATBOT")
    print("Categories: General, Admission, Library, Examination, Fees")
    print("Type 'exit' to stop.\n")

    try:
        llm = ChatOllama(model=MODEL_NAME, temperature=0.2)
        chain = prompt | llm
    except Exception as exc:
        print("Could not initialize Ollama. Check that Ollama is running and")
        print(f"that the model '{MODEL_NAME}' is installed. Details: {exc}")
        return

    history_path = DATA_DIR / "chatbot_responses.csv"
    DATA_DIR.mkdir(exist_ok=True)

    while True:
        category = input("Enter category: ").strip()
        if category.lower() == "exit":
            break
        question = input("Enter your question: ").strip()
        if question.lower() == "exit":
            break
        if not category or not question:
            print("Please enter both category and question.\n")
            continue

        try:
            result = chain.invoke({"category": category, "question": question})
            answer = result.content if hasattr(result, "content") else str(result)
            print("\nChatbot:", answer, "\n")
            new_file = not history_path.exists()
            with history_path.open("a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if new_file:
                    writer.writerow(["category", "user_query", "chatbot_response"])
                writer.writerow([category, question, answer])
        except Exception as exc:
            print(f"Error while generating response: {exc}\n")

    print("Chat history saved in dataset/chatbot_responses.csv")

if __name__ == "__main__":
    main()

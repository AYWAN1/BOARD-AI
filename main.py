
import requests

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "qwen2.5:3b"


def ask_ai(question):
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": question,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        return response.json().get("response", "No response received.")

    except requests.exceptions.RequestException as error:
        return f"Connection error: {error}"


def main():
    print("=" * 45)
    print("BOARD-AI - Local AI Assistant")
    print("=" * 45)
    print(f"Model: {MODEL_NAME}")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("BOARD-AI closed.")
            break

        if not question:
            continue

        print("\nBOARD-AI is thinking...\n")
        answer = ask_ai(question)
        print(f"AI: {answer}\n")


if __name__ == "__main__":
    main()


import requests

OLLAMA_URL = "http://localhost:11434"


def check_ollama():
    print("BOARD-AI - Ollama Connection Check")
    print("-" * 40)

    try:
        response = requests.get(
            f"{OLLAMA_URL}/api/tags",
            timeout=5
        )
        response.raise_for_status()

        models = response.json().get("models", [])

        if not models:
            print("Ollama is running, but no models are installed.")
            return

        print("Ollama connected successfully!")
        print("\nAvailable models:")

        for model in models:
            print(f"- {model.get('name', 'Unknown')}")

    except requests.exceptions.ConnectionError:
        print("Cannot connect to Ollama.")
        print("Make sure Ollama is installed and running.")

    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")


if __name__ == "__main__":
    check_ollama()

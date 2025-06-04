import requests
import json

OLLAMA_URL = "http://172.211.240.116/v1/completions"
MODEL_NAME = "granite3.3:8b"

def ask_model(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        print("Raw response: ",response.text)
        data = json.loads(response.text)
        return data['choices'][0]["text"].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the Granite AI Chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = ask_model(user_input)
        print("Granite:", response)

if __name__ == "__main__":
    main()

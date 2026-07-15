import ollama

def generate_response(user_message: str, system_prompt: str = "") -> str:
    try:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        response = ollama.chat(
            model="llama3.2",
            messages=messages,
            keep_alive="30m" 
        )
        return response["message"]["content"]

    except Exception as e:
        return f"Error connecting to AI model: {e}"
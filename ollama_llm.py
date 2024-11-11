import ollama


def language_model_chat(user_input, PROMPT=None):
    model = "llama3.1:latest"
    stream = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": user_input},
        ],
        stream=True,
    )

    output = ""
    for chunk in stream:
        output += chunk["message"]["content"]
    return output


if __name__ == "__main__":
    PROMPT = """You are a helpful AI assistant named Neu. Your responses should be conversational, friendly, and natural-sounding, 
                as if you're chatting with a friend. Don't make your language formal, so use things like "I'm" instead of I am, 
                or "We'll" instead of "We will". Keep your responses very short and quick. Use no dashs in your replies.
                Youy will be given the full conversational history, but only output your answer, and nothing else.
                Keep responses less than 10 words. No emojis.
                """

    while True:
        user_input = input("User Input: ")
        print(user_input)
        llm_output = language_model_chat(user_input)
        print(llm_output)

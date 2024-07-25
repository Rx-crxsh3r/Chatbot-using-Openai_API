import openai
from rich.console import Console
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel

# Set your OpenAI API key here
openai.api_key = ""

console = Console()
messages = [
    {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
]

def display_greeting():
    console.print(Panel("Hi, I'm ChatGPT. I'm a helpful assistant", title="ChatGPT"))

def get_chat_completion(messages):
    try:
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        return chat_completion["choices"][0]["message"]["content"]
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        exit()

def main():
    display_greeting()
    reply = get_chat_completion(messages)
    console.print(f"[bold green]ChatGPT:[/bold green] {reply}")
    messages.append({"role": "assistant", "content": reply})

    while True:
        message = Prompt.ask("👤")
        if message.lower() == "exit":
            break
        elif message.lower() == "clear":
            console.clear()
            display_greeting()
            messages.clear()
            messages.append({"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"})
            reply = get_chat_completion(messages)
            console.print(f"[bold green]ChatGPT:[/bold green] {reply}")
            messages.append({"role": "assistant", "content": reply})
            continue

        if message:
            messages.append({"role": "user", "content": message})
            reply = get_chat_completion(messages)
            console.print(f"[bold green]ChatGPT:[/bold green] {reply}")
            messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()

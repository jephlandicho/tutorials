import openai
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("api_key")
openai.api_base = "https://llama3-1-405b.lepton.run/api/v1/"

def create_essay():
    user_prompt = input("Please enter your essay prompt: ")

    system_prompt = {
        "role": "system",
        "content": "You are an expert essay writer. Write a detailed, coherent, and well-organized essay based on the user's prompt."
    }
    
    user_message = {
        "role": "user",
        "content": user_prompt
    }

    try:
        response = openai.ChatCompletion.create(
            model="llama3-1-405b",
            messages=[system_prompt, user_message],
            max_tokens=2000,
            stream=True
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"essay_{timestamp}.txt"
        
        with open(filename, "w") as file:
            print("\nGenerated Essay:\n")
            for chunk in response:
                if "choices" in chunk:
                    chunk_content = chunk['choices'][0]['delta'].get('content', '')
                    print(chunk_content, end='') 
                    file.write(chunk_content)
                    
        print(f"\n\nEssay saved as {filename}")

    except Exception as e:
        print("Error occurred:", e)


create_essay()

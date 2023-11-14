import openai
import os
from dotenv import load_dotenv

load_dotenv('.env')
openai.api_key=os.getenv('OPENAI_API_KEY')
def gpt_turbo(prompt):
    return openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {'role'  : 'user', 
                'content':  prompt}
            ],
            temperature = 0.2
            )
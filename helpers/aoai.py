import os
import json
from dotenv import load_dotenv
import openai

# load .env
load_dotenv()

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_OPENAI_VERSION")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

deployment_name = 'gpt-35-turbo'

def get_completion(messages):
    return openai.ChatCompletion.create(engine=deployment_name, messages=messages, max_tokens=150)

def get_completion_with_functions(messages, functions):
    response = openai.ChatCompletion.create(engine=deployment_name, messages=messages, functions=functions)
    finish_reason = response['choices'][0]['finish_reason']
    
    result = {
        'finish_reason': finish_reason,
        'message': None,
        'function_name': None,
        'function_args': None
    }

    if finish_reason == "function_call":
        result['function_name'] = response['choices'][0]['message']['function_call']['name']
        result['function_args'] = json.loads(response['choices'][0]['message']['function_call']['arguments'])
    else:
        result['message'] = response['choices'][0]['message']['content'].replace('  ', ' ')
    
    return result
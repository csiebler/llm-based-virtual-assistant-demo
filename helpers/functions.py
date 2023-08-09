from helpers.aoai import get_completion_with_functions
from tasks.Balance import Balance
from tasks.Data import Data
from tasks.Roaming import Roaming

def handle_task(user_message, task_key):
    
    if task_key in ["balance", "data", "roaming"]:
        c = eval(task_key.title())
        messages = handle(user_message=user_message, task_key=task_key, cls=c)[1:]
    else:
        response = "Sorry, I cant do that yet."
        print(f"Assistant: {response}")
        messages = [{"role": "assistant", "content": response}]
    return messages

def handle(user_message, task_key, cls):
    instance = cls()
    messages = instance.get_initial_messages(user_message)
    functions = instance.get_openai_functions()
    
    action_performed = False
    while not action_performed:
        response = get_completion_with_functions(messages=messages, functions=functions)        
        if response['finish_reason'] == "function_call":
            function_name = response['function_name']
            function_args = response['function_args']
            print(f"---> Calling API {function_name} with arguments {function_args}")
            
            # in the corresponding class, call the implementation of the function name with its args        
            response_text = getattr(instance, function_name)(**function_args)
            
            print(f"Assistant ({function_name}): {response_text}")
            messages.append({"role": "assistant", "content": response_text})
            action_performed = True
        else:
            response_text = response['message']
            print(f"Assistant ({task_key}): {response_text}")
            messages.append({"role": "assistant", "content": response_text})
            user_message = input("Customer: ")
            messages.append({"role": "user", "content": user_message})
    return messages

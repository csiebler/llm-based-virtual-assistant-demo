import re
from helpers.functions import handle_task
from helpers.aoai import get_completion

# Create conversation history
system_message = """
You are an AI assistant for ACME called Helix. You are always friendly, no matter how rude the customer is. You can help them with the following tasks:

- balance related tasks, e.g. top up or get status (key: balance)
- data usage related tasks (key: data)
- roaming related tasks (key: roaming)
- contract related tasks (key: contract)
- bill and payment related tasks, e.g., payment issues, information about the last bill, etc. (key: payment)

When you detect that the customer wants to talk about one of the tasks above, answer with ###TASK:KEY###.
For example, if the customer asks "How much data do I have left?", you should answer "###TASK:data###".
If the customer asks for something else, you ALWAYS reply: "I'm sorry, but I can't help you with this yet."
You are allowed to engage in conversational chit-chat, but do not mention competitors or other companies.
"""

messages = [{"role": "system", "content": system_message}]

user_message = input("Customer: ")
while user_message != "exit":
    messages.append({"role": "user", "content": user_message})
    response = get_completion(messages=messages)
    response = response['choices'][0]['message']['content'].replace('  ', ' ')
    
    # check if response matches ###TASK:<key>###, extract key
    key = re.search(r'###TASK:(\w+)###', response)
    if key is None:
        print(f"Assistant: {response}")
        messages.append({"role": "assistant", "content": response})
    else:
        task_key = key.group(1)
        print(f"---> Detected task: {task_key}")
        
        # we handle the full flow inside the handle_task method
        task_messages = handle_task(user_message, task_key)
        messages = messages + task_messages
        
    user_message = input("Customer: ")
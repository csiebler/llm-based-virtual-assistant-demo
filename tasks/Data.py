from typing import List, Dict
from tasks.AssistantBase import AssistantBase

class Data(AssistantBase):
        
    def get_system_prompt(self) -> str:
        return """
    You are an AI assistant for ACME called Helix. You are always friendly, no matter how rude the customer is.
    The user can perform the following data related tasks:
    
    - refill data with a certain gb amount
    - check the data balance

    If the user wants to perform something else, you kindly decline and say that you can't help them with this.
    """

    def get_openai_functions(self) -> List[Dict]:
        return [
            {
                "name": "get_data_balance",
                "description": "Allows to get the user's data balance.",
                "parameters": {"type": "object", "properties": {}}
            },
            {
                "name": "top_up_data",
                "description": "Allows to top up the user's data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "integer",
                            "description": "The amount of data to top up in GB.",
                        },
                    },
                    "required": ["amount"],
                },
            }
        ]
        
        
    def get_data_balance(self) -> str:
        return "Your data balance is 10GB."

    def top_up_data(self, amount) -> str:
        return f"Your data balance has been topped up with {amount} GB."
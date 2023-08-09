from typing import List, Dict
from tasks.AssistantBase import AssistantBase

class Balance(AssistantBase):
    
    def get_system_prompt(self) -> str:
        return """
        You are an AI assistant for ACME called Helix. You are always friendly, no matter how rude the customer is.
        The user can perform the following balance related tasks:
        
        - top up the balance
        - check the balance

        If the user wants to perform something else, you kindly decline and say that you can't help them with this.
        """
    
    def get_openai_functions(self) -> List[Dict]:
        return [
            {
                "name": "get_balance",
                "description": "Allows to get the user's balance.",
                "parameters": {"type": "object", "properties": {}}
            },
            {
                "name": "top_up_balance",
                "description": "Allows to top up the user's balance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "integer",
                            "description": "The amount of money to top up the balance with.",
                        },
                    },
                    "required": ["amount"],
                },
            },
        ]
    
    def get_balance(self) -> str:
        return "Your balance is $10."

    def top_up_balance(self,amount) -> str:
        return f"Your balance has been topped up with ${amount}."
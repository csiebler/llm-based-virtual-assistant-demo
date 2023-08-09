from typing import List, Dict
from tasks.AssistantBase import AssistantBase

class Roaming(AssistantBase):
        
    def get_system_prompt(self) -> str:
        return """
    You are an AI assistant for ACME called Helix. You are always friendly, no matter how rude the customer is.
    The user can perform the following roaming related tasks:
    
    - cost for roaming in a certain country (might be free or not)

    If the user wants to perform something else, you kindly decline and say that you can't help them with this.
    """

    def get_openai_functions(self) -> List[Dict]:
        return [
            {
                "name": "roaming_cost_for_country",
                "description": "Returns the user's roaming cost for a given country.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "country": {
                            "type": "string",
                            "description": "The country to check the roaming cost for, e.g. Germany, France, USA, etc.",
                        }
                    },
                    "required": ["country"],
                },
            }
        ]
        
        
    def roaming_cost_for_country(self, country) -> str:
        if country in ["Germany", "France", "Spain"]:
            return f"Roaming is free for {country}, you use it for the same conditions as in your local country."
        else:
            return f"Roaming in {country} costs $0.10 per minute or message, and $5 per GB."


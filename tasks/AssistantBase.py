from abc import ABC, abstractmethod

class AssistantBase(ABC):
    
    @abstractmethod
    def get_system_prompt(self):
        pass
    
    @abstractmethod
    def get_openai_functions(self):
        pass
    
    def get_initial_messages(self, user_message):
        messages = [{"role": "system", "content": self.get_system_prompt()}]
        messages.append({"role": "user", "content": user_message})
        return messages
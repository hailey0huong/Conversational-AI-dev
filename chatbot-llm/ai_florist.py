import os
import anthropic
from utils import ClaudeChat

class PromptConstructor:
    """This class is to construct a prompt given user inputs.
    """
    def __init__(self) -> None:
        pass

    def prompt_engineering(self):
        pass
    

class AIFloristClaude(ClaudeChat):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)
    
    def _print_ai_response(self) -> None:
        print("AI Florist: "+ self.chat_history[-1])
        
        
    
    
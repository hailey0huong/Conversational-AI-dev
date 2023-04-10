import os
import anthropic


class AIFloristClaude:
    def __init__(self, api_key) -> None:
        self.client = anthropic.Client(api_key)
        self.chat_history = []
        self.last_response = None
        
    def _write_prompt_for_Claude(self):
        i=0
        prompt = ""
        while i < len(self.chat_history):
            if i%2 == 0:
                prompt = prompt + anthropic.HUMAN_PROMPT + " " + self.chat_history[i]
            else:
                prompt = prompt + anthropic.AI_PROMPT + " " + self.chat_history[i]
            i+=1
            
        prompt += anthropic.AI_PROMPT
        
        return prompt
        
    def generate_response(self, prompt, max_tokens=1000, temperature=1) -> None:
        self.chat_history.extend(prompt)
        final_prompt = self._write_prompt_for_Claude()
        
        response = self.client.completion(
            prompt = final_prompt,
            stop_sequences = [anthropic.HUMAN_PROMPT],
            model="claude-v1",
            max_tokens_to_sample=max_tokens,
            temperature=temperature,
        )
        self.chat_history.append(response['completion'])
        self.last_response = response
        self._print_human_prompt(prompt)
        self._print_ai_response()

    
    def reset(self) -> None:
        self.chat_history = []
        self.last_response = None
        
    def _print_human_prompt(self, prompt) -> None:
        print("HUMAN: " + prompt[0])
    
    def _print_ai_response(self) -> None:
        print("AI Florist: "+ self.chat_history[-1])
        
        
    
    
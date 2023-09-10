import os
import anthropic
import openai

MODEL = "claude-2.0"

class ClaudeChat():
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
            model=MODEL,
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
        print("AI: "+ self.chat_history[-1])
        
        
def get_completion_gpt(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages_gpt(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    return response.choices[0].message["content"]

def get_completion_and_token_count_gpt(messages, 
                                   model="gpt-3.5-turbo", 
                                   temperature=0, 
                                   max_tokens=500):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    
    content = response.choices[0].message["content"]
    
    token_dict = {
'prompt_tokens':response['usage']['prompt_tokens'],
'completion_tokens':response['usage']['completion_tokens'],
'total_tokens':response['usage']['total_tokens'],
    }

    return content, token_dict


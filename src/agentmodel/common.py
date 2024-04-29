from agentmodel import Agent

class AgentClass:
    def __init__(self, llm_model:str = None, system_prompt:str = None, user_prompt:str = None):
        self.model = llm_model
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.agent = Agent(self.model, self.system_prompt, self.user_prompt)
        
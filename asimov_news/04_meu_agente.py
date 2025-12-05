# %%
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from prompt_esportivo import prompt_pro_agente

# %%
print(prompt_pro_agente)
# %%
load_dotenv()

agente = Agent(
    model=OpenAIChat(id='gpt-4.1-mini'),
    tools=[TavilyTools()]
)

# AQUI ele executa o prompt
resposta = agente.run(prompt_pro_agente)
print(resposta)
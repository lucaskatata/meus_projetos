# %%
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=OpenAIChat(id='gpt-4.1-mini'),
    tools=[TavilyTools()],
    debug_mode=True
)

agente.print_response('Use suas ferramentas para pesquisar noticias sobre a cidade de Ibitinga, localizada no interior de São Paulo')
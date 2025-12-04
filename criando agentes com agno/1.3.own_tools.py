# %%
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq 
from dotenv import load_dotenv

load_dotenv()

def celsius_to_fh(temperatura_celsius: float):
    """
    Converte uma temperatura em graus Celsius para Farenheit.

    Args:
        temperatura_celsius (float): Temperatura em graus Celsius

    Returns:
        float: Temperatura convertida em graus Farenheit
    """
    return (temperatura_celsius * 9/5) + 32

agent = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[TavilyTools(),
           celsius_to_fh], 
)

agent.print_response('Qual a temperatura na cidade de Ibitinga em graus Farenheit')
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")

agent = Agent(
    model = llm,
    name = "My First Agno Agent",
    markdown=True,
    stream = True
)

agent.print_response("Write the 200 word paragraph about the Gen AI.")

agent.print_response("About what topic i asked you earlier.")


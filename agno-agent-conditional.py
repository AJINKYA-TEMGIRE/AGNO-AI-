from agno.agent import Agent
from agno.workflow import Step , Workflow , Condition
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

model = Groq(id = "llama-3.1-8b-instant")


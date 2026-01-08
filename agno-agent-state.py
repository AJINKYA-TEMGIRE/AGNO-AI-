# To add the key points in the session state

from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from textwrap import dedent

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")

db = SqliteDb(db_file="database.db")

def add_to_session_state(session_state : dict , points : str) -> str:
    points_list = session_state["key_points"]
    points_list.append(points)
    return f"{points} added to the session state"

agent = Agent(
    model = llm,
    db = db,
    session_id="session-1",
    session_state={"key_points" : []},
    tools = [add_to_session_state],
    instructions=dedent("""
                You are an expert assistant.
                        Your task is to create the summary.
                        You have an access to the tool 'add_to_session_state' whose work is to add the key point from the summary
                        Add the key points only if asked. """),
    add_session_state_to_context=True,
    add_history_to_context=True,
    num_history_runs=3,
    name = "My First Agno Agent",
    markdown=True,
    stream = True
)

agent.print_response("Write the 200 word paragraph about the Gen AI.")

agent.print_response("About what topic i asked you earlier.")

agent.print_response("Add the key points to the session state.")

print(agent.get_session_state("session-1"))




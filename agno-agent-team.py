# Building a team for pratice
from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")

news_agent = Agent(
    id="news_agent",
    name="News Agent",
    model=llm,
    role="Get the latest news headlines and give summary",
    instructions=["You are a news search agent",
                  "Search for the latest news for a particular destination and give a summarized view"],
    tools=[DuckDuckGoTools()]
)

web_search_agent = Agent(
    id="web_search_agent",
    name="Web Search Agent",
    model=llm,
    role="Get information for places to visit at the destination",
    instructions=["You are a web search agent",
                  "your goal is to search for places of interest for a particular destination"],
    tools=[DuckDuckGoTools()]
)


travel_agent = Team(
    members=[news_agent, web_search_agent],
    model=llm,
    name="Travel Agent",
    id="travel_agent",
    role="You are a team leader and you delegate tasks to members",
    instructions=["You are an expert travel agent",
                  "you team members can get latest news and places of interest for a particular destination",
                  "your task is to present the output using proper headlines"],
    stream=True,
    markdown=True,
)

travel_agent.cli_app(stream=True, markdown=True)

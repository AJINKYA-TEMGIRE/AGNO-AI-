from agno.agent import Agent
from agno.models.groq import Groq 
from agno.workflow import Step , Workflow , StepInput , Router
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant" )


sql_agent = Agent(
    model = llm,
    id = "Sql Agent",
    name = "Sql Agent",
    markdown=True,
    instructions=["You are the senior MySQL Developer",
                  "You have to give the sql query for the asked questions",
                  "You have to return only the query , don't include other text"]
)

pandas_agent = Agent(
    model = llm,
    id = "Pandas Agent",
    name = "Pandas Agent",
    markdown=True,
    instructions=["You are senior data analyst and an expert in Pandas",
                  "You have to give the pandas code to the asked question.",
                  "Give only the code, don't give extra text"]
)

format_agent = Agent(
    model = llm,
    id = "Generate Agent",
    name = "Generate Agent",
    markdown=True,
    instructions=["You have to format the code in proper format and then give to the user",
                  "Don't add extra text, just give the code"]
)

# steps

sql_step = Step(
    name = "Sql Step",
    agent=sql_agent,
    description="Gives the sql code."
)

pandas_step = Step(
    name = "Pandas Agent",
    agent = pandas_agent,
    description="To give the pandas code"
)

format_step = Step(
    name = "Format Step",
    agent = format_agent,
    description="To format the code properly"
)

def choice_step(step : StepInput) -> list[Step]:
    content = step.input or ""
    if content:
        if "sql" in content.lower():
            return [sql_step]
        else:
            return [pandas_step]
    else:
        return [pandas_step]

router = Router(
    choices=[sql_step , pandas_step],
    name = "Routing step",
    description="To route to proper agent",
    selector=choice_step
)


workflow = Workflow(
    id = "Workflow",
    name = "Routing workflow",
    description="The workflow to route to the proper agent",
    steps=[router , format_step]
)

workflow.cli_app(markdown=True,
                        stream = True)




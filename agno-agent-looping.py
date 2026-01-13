from agno.agent import Agent
from agno.models.groq import Groq
from agno.workflow import Step , Workflow , Loop , StepOutput
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id = "llama-3.1-8b-instant")

def end(outputs : list[StepOutput]) -> bool:
    if outputs:
        for output in outputs:
            content = output.content
            if len(content.strip().split(" ")) > 20:
                return True
            else:
                return False
    else:
        return False


shayari_agent = Agent(
    model = llm,
    markdown=True,
    id = "Shayari Agent",
    name = "Shayari Agent",
    instructions=["You are a great shayar like Mirza Ghalib",
                  "You have to generate heart touching shayaries based on the topic given.",
                  "Only generate the shayari not other content.",
                  "write in a proper format with proper line breaks"]

)

# creating the step


shayari_step = Step(
    name = "Shayari Step",
    agent=shayari_agent,
    description="This step will generate the shayari on the given topic",
)

loop_step = Loop(
    steps = [shayari_step],
    name = "Looping step",
    description="To write the best heart touching shayari in loop",
    max_iterations=3,
    end_condition=end
)

workflow = Workflow(
    id = "Shayari",
    name = "Shayari",
    description="To generate the shayari in the loop",
    steps = [loop_step],
)

workflow.print_response("input: write a shayari on betryal of love" , 
                        markdown=True,
                        stream = True)
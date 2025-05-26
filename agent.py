from google.adk.agents import Agent
from _init_ import validate_hsn_code

def validate_single_hsn(code: str) -> dict:
    """Tool to validate a single HSN code."""
    return validate_hsn_code(code)

root_agent = Agent(
    name="hsn_validator_agent",
    model="gemini-2.0-pro",
    description="Agent to validate HSN codes based on a master Excel dataset.",
    instruction="You are an intelligent assistant that validates HSN codes and returns whether they're valid along with their descriptions if available.",
    tools=[validate_single_hsn],
)


from utils.llm import ask
def run(plan):
    return ask("Senior python dev","Write FastAPI project based on:"+plan)

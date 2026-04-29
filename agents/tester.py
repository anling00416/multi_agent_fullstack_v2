
from utils.llm import ask
def run(code):
    return ask("QA engineer","Write pytest tests:"+code)

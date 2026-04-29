
from utils.llm import ask
def run(code):
    return ask("Strict reviewer","Improve and fix code:"+code)

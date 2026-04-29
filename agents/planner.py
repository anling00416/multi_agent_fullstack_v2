
from utils.llm import ask
def run(requirement):
    return ask("Senior architect","Break requirement into architecture, files, steps:"+requirement)

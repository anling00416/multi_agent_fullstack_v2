
import os
from openai import OpenAI
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(system,user):
    r=client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role":"system","content":system},{"role":"user","content":user}],
        temperature=0.3
    )
    return r.choices[0].message.content

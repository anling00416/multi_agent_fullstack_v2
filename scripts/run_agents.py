
from agents.planner import run as plan
from agents.coder import run as code
from agents.reviewer import run as review
from agents.tester import run as test

req="Build todo app"
p=plan(req)
c=code(p)
r=review(c)
t=test(r)
open("generated_code.py","w").write(r)
open("generated_tests.py","w").write(t)
print("Pipeline finished")

import nltk
from nltk import CFG
import sys

grammar = CFG.fromstring("""
N -> N N | 'natural' | 'language' | 'processing' | 'course'
""")

if len(sys.argv) > 1:
    inp = 'natural language processing course'
else:
    for line in sys.stdin:
        inp = line.strip()
print("Start:", grammar.start(), file=sys.stderr)
print("Productions:", grammar.productions(), file=sys.stderr)
parser = nltk.ChartParser(grammar)
for tree in parser.parse(inp.split()):
    print(tree)

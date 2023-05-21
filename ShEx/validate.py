from rdflib import Graph, Namespace
from pyshex import ShExEvaluator
g = Graph()
g.parse("example1.ttl", format="turtle")
shexfile = open("user.shex","r")
shex = shexfile.read()

ex = Namespace("http://example.org/")
print(f"ShEx file read: {shex}")

results = ShExEvaluator().evaluate(g, shex, focus = ex.alice, start = ex.User)
for r in results:
    if r.result:
        print("PASS")
    else:
        print(f"FAIL: {r.reason}")

shexfile.close()


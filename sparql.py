from rdflib import Graph

g = Graph()

g.parse("example1.ttl", format="turtle")
g.parse("example2.ttl", format="turtle")

print(g.serialize(format="turtle"))


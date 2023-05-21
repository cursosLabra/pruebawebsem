from rdflib import Graph, Namespace
from pyshacl import validate
data = Graph()
data.parse("example1.ttl", format="turtle")

shapes = Graph()
shapes.parse("shapes.ttl", format="turtle")

r = validate(data, shacl_graph = shapes, debug = True)
conforms, results_graph, results_text = r
print(f"Conforms: {conforms}")

print(results_graph.serialize(format="turtle"))

from rdflib import Graph
from owlready2 import get_ontology, sync_reasoner

onto = get_ontology("owlExample.xml").load()

print("Before reasoning:")
for i in onto.individuals():
    print(f"Individual: {i} is a: {i.is_a}")

sync_reasoner()   

print("After reasoning:")
for i in onto.individuals():
    print(f"Individual: {i} is a: {i.is_a}")

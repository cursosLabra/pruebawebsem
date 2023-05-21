from rdflib import Graph

g = Graph()

g.parse("datos.ttl", format="turtle")
query1 = """
prefix uni: <http://uniovi.es>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?x ?p ?y
WHERE {
    ?x ?p ?y .
}"""
result = g.query(query1)

for row in result:
    print(f"{row.x} {row.p} {row.y}")



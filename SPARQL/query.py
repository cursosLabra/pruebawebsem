from rdflib import Graph

g = Graph()

g.parse("datos.ttl", format="turtle")
query1 = """
PREFIX dc:  <http://purl.org/dc/terms/>
PREFIX uni: <http://uniovi.es/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 


SELECT ?p ?c WHERE {
 ?p  dc:creator  ?c .
 ?c  rdf:type    uni:Profesor .
}"""
result = g.query(query1)

for row in result:
    print(f"{row.p} {row.c}")



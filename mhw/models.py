from py2neo import Graph, Node, Relationship
import uuid

graph = Graph()

def get_search_results(searchArmor):
    query = """
    MATCH (armorPiece:armorPiece)-[:CONTAINS_MATERIAL]->(material:material)-[:FROM_MONSTER]->(monster:monster)
    WHERE armorPiece.name CONTAINS $armor
    RETURN armorPiece, collect(DISTINCT material) as materials, collect(DISTINCT monster) as monsters
    ORDER BY armorPiece.name ASC LIMIT 2000
    """

    return graph.run(query, armor=searchArmor)
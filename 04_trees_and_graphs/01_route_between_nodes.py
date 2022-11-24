"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
from Graph import Graph


def route_between_nodes(graph, source, destination):
    return graph.breadth_first_search(source, destination)


def test_route_between_nodes():
    graph = Graph()
    
    graph.add_edge(1, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 2)
    graph.add_edge(2, 3)
    graph.add_edge(4, 3)
    graph.add_node(6)
    
    assert route_between_nodes(graph, 1, 2)
    assert route_between_nodes(graph, 3, 2)
    assert not route_between_nodes(graph, 1, 4)
    assert not route_between_nodes(graph, 6, 1)

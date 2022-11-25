"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""

import pytest

from graph import Graph


def build_order(projects, dependencies):
    g = Graph()
    for project in projects:
        g.add_node(project)
    for dependency in dependencies:
        g.add_edge(dependency[1], dependency[0])
    
    completed = {project: False for project in projects}
    order = []
    
    def topological_sort(node):
        if completed[node.value]:
            return
        
        completed[node.value] = True
        for dependent_project in node.adjacent:
            topological_sort(dependent_project)
        order.append(node.value)
    
    for project in g:
        topological_sort(project)
    
    return order


@pytest.mark.parametrize('projects, dependencies, expected_build_order', [
    (['a', 'b', 'c', 'd', 'e', 'f'],
     [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')],
     ['f', 'a', 'b', 'd', 'c', 'e'])
])
def test_build_order(projects, dependencies, expected_build_order):
    assert build_order(projects, dependencies) == expected_build_order

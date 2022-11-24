from collections import deque


class Graph:
    class Node:
        
        def __init__(self, value, adjacent=None):
            self.value = value
            self.adjacent = adjacent if adjacent else []
        
        def __repr__(self):
            return f'{self.value}: ' + str([i.value for i in self.adjacent])
        
        def add_adjacent(self, child):
            self.adjacent.append(child)
    
    def __init__(self, nodes=None):
        self.nodes = {}
        if nodes:
            self.add_all_nodes(nodes)
    
    def __repr__(self):
        return '\n'.join([str(i) for i in self.nodes.values()])
    
    def __len__(self):
        return len(self.nodes)
    
    def __iter__(self):
        for node in self.nodes.values():
            yield node
    
    def add_node(self, value):
        self.nodes[value] = Graph.Node(value)
    
    def add_all_nodes(self, nodes):
        # TODO: Fix this
        for i in nodes.keys():
            self.add_node(i)
        for i, adjacent in nodes.items():
            for j in adjacent:
                self.nodes[i].add_adjacent(self.nodes[j])
    
    def get_node(self, value):
        if value not in self.nodes.keys():
            self.add_node(value)
        return self.nodes[value]
    
    def add_edge(self, source, destination):
        source_node = self.get_node(source)
        destination_node = self.get_node(destination)
        source_node.add_adjacent(destination_node)
    
    def depth_first_search(self, source, destination):
        if source not in self.nodes.keys() or destination not in self.nodes.keys():
            return None
        
        stack = [self.nodes[source]]
        visited = set()
        path_map = {}
        
        while stack:
            node = stack.pop()
            if node.value in visited:
                continue
            if node.value == destination:
                path = [destination]
                i = destination
                while i != source:
                    i = path_map[i]
                    path.append(i)
                return ' -> '.join(map(str, reversed(path)))
            visited.add(node.value)
            stack.extend(node.adjacent)
            path_map.update({i.value: node.value for i in node.adjacent})
        return False
    
    def breadth_first_search(self, source, destination):
        if source not in self.nodes.keys() or destination not in self.nodes.keys():
            return None
        
        queue = deque([self.nodes[source]])
        visited = set()
        path_map = {}
        
        while queue:
            node = queue.popleft()
            if node.value in visited:
                continue
            if node.value == destination:
                path = [destination]
                i = destination
                while i != source:
                    i = path_map[i]
                    path.append(i)
                return ' -> '.join(map(str, reversed(path)))
            visited.add(node.value)
            queue.extend(node.adjacent)
            path_map.update({i.value: node.value for i in node.adjacent})
        return False


# g = Graph({
#     1: [3],
#     2: [3],
#     3: [5],
#     4: [3],
#     5: [2],
#     6: []
# })
# print(g)

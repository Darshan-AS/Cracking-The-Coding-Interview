class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else {}
    
    def __repr__(self):
        return f'{self.value}: ' + str([i for i in self.children.keys()]) + '\n' + '\n'.join(
            [str(i) for i in self.children.values()])
    
    def add_child(self, tree):
        self.children[tree.value] = tree
    
    def get_children(self):
        return self.children

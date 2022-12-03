class Tree:
    def __init__(self):
        self.root = None
        self.height = 0
    
    def add_root(self, root):
        self.root = root
    
    def add_child(self, parent, child):
        parent.add_child(child)
        child.level = parent.level + 1
        if child.level > self.height:
            self.height += 1
    
class Vertex:
    def __init__(self, label):
        self.label = label
        self.children = []
        self.level = 0
    
    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return str(self.label)
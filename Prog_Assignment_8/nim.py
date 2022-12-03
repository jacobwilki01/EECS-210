from tree import Tree, Vertex

class NimGame:
    def __init__(self,piles,name=""):
        self.tree = MinMaxTree()
        self.tree.add_root(NimVertex(piles))
        self.name = name
        self.play()
    
    def play(self):
        self.play_rec(self.tree.root)
        self.det_values()
    
    def play_rec(self,vertex):
        if vertex.label[0] == 0 and vertex.label[1] == 0 and vertex.label[2] == 0:
            if vertex.level % 2 == 0:
                vertex.update(1)
            else:
                vertex.update(-1)
            return
        else:
            for i in range(0,3):
                for j in range(1,vertex.label[i]+1):
                    new_piles = list(vertex.label)
                    new_piles[i] -= j
                    new_piles = tuple(new_piles)
                    new_vertex = NimVertex(new_piles)
                    self.tree.add_child(vertex,new_vertex)
                    self.play_rec(new_vertex)
    
    def det_values(self):
        for x in range(len(self.tree.levels)-2, -1, -1):
            for vertex in self.tree.levels[x]:
                if len(vertex.children) > 0:
                    if vertex.level % 2 == 0:
                        vertex.value = max([child.value for child in vertex.children])
                    else:
                        vertex.value = min([child.value for child in vertex.children])

class NimVertex(Vertex):
    def __init__(self, label):
        super().__init__(label)
        self.value = 0
    def update(self,value):
        self.value = value

class MinMaxTree(Tree):
    def __init__(self):
        super().__init__()
        self.levels = []
    
    def add_root(self, root):
        super().add_root(root)
        self.levels.append([root])
    
    def add_child(self, parent, child):
        super().add_child(parent,child)
        if child.level == len(self.levels):
            self.levels.append([child])
        else:
            self.levels[child.level].append(child)
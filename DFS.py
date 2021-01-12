class Node:
    def __init__(self,name):
        self.name=name
        self.children=[]

    def addChild(self,name):
        self.children.append(name)
    
    def DFS(self,arr):
        arr.append(self.name)
        for child in self.children:
            child.DFS(arr)
        return arr
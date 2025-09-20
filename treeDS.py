class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev= None


class Tree:
    
    def __init__(self):
        self.root = None
    
    def Root (self,data):
        node = Node(data)
        self.root = node
        
    def InsertLeftRoot(self,data):
        node = Node (data)
        
        self.root.prev=node 
    
    def InsertRightRoot(self,data):
        node = Node(data)
        self.root.next = node
    
    def InsertleftLeft(self.data)
        


if __name__ == "__main__":
    
    
    
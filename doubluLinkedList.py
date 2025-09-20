class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        

class LL:
    def __init__(self):
        self.head = None
        self.temp = self.head
        
        
    
    def addNode(self,data):
        new_node = Node (data)
        
        if self.head is None :
            self.head = new_node
            self.temp = new_node
            
        else :
            self.temp.next= new_node
            new_node.prev= self.temp
            self.temp = new_node        
    
    
    def DeleteAtpos(self,pos):
        
        temp = self.head
        ptr = 0
        while ptr < pos-1:
            temp = temp.next
            ptr += 1

        print(temp.data)
        
        temp.prev.next = temp.next
        temp.next.prev= temp.prev
        temp.prev=None 
        temp.next=None 

        
    def Display(self):
        temp = self.head
        
        while (temp):
            print(temp.data)
            temp=temp.next
            
    
    


if __name__ == "__main__":
    
    print("Hello World ")
    print("Implementing Linked list ")
    
    dll = LL()
    dll.addNode(10)
    dll.addNode(20)
    dll.addNode(30)
    dll.addNode(40)
    dll.Display()
    
    
    dll.DeleteAtpos(2)
    
    dll.Display()

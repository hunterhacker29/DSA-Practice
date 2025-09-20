

class Node :
    def __init__ (self,data,next):
        self.data= data
        self.next = next 
        
        
class LinkedList :
    def __init__(self):
        self.head = None 
        self.tail = None
        
        
        
    def InsertAtbeg(self,data):
        
        node = Node(data,self.head)
        self.head = node 
     
    
    def InsertAtend(self,data):
        
        node = Node(data,None)
        
        if self.head is None:
            self.head= node 
            
        temp = self.head
        
        while temp.next is not None :
            temp = temp.next
        
        temp.next = node
        
        
    def InsertAtpos(self,data,pos):
        
        count   = 1
        temp = self.head
        node = Node(data,None)
        while temp is not None :
            temp = temp.next
            count += 1
        

        
        if pos > count or pos < 1:
            print("Invalid position")
            return
        else :
            temp2 = self.head
            curr = 1
            
            while curr < pos -1  :
                temp2 = temp2.next
                curr += 1
                
            node.next = temp2.next
            temp2.next = node
                 
            
             
    
    def reverse(self):
        prev = None 
        current = self.head
        next = self.head
        
        
        while current is not None:
            next = current.next
            current.next= prev 
            prev = current
            current = next
            self.head = prev

            
    def printList (self):
        
       ptr = self.head
     
       
       while ptr is not None:
        print(ptr.data)
        ptr= ptr.next
           
           
       
            
    
    
if __name__ == '__main__':
    ll= LinkedList()
    ll.InsertAtbeg(10)
    ll.InsertAtend(20)
    ll.InsertAtend(30)
    ll.InsertAtpos(25, 2)
    ll.InsertAtend(40)
    ll.InsertAtend(50)
    
    
    
    
    ll.printList()
    
    ll.reverse()
    print("Reversed Linked List:")
    ll.printList()
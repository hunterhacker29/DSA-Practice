

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
                 
    
    def removeAtpos(self,pos):
        
        count = 1
        prev= self.head
        temp = self.head
        
        while count < pos-1  :
            # prev= prev.next
            # temp = temp.next
            # print(temp.data)
            
            temp= temp.next
            
            count += 1
            
        next = temp.next
        
        temp.next= next.next
        next.next=None 

    
    def removeAtbeg(self):
        temp = self.head
        self.head = temp.next
        temp.next=None 
         
        
            
    def removeAtEnd(self):
        
        temp = self.head
        while temp.next is not None:
            prev= temp
            temp = temp.next
            
        
        
        prev.next = None 
        temp.next= None 
             
        
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
    ll.InsertAtend(40)
    ll.InsertAtend(50)
    ll.InsertAtend(60)
    
    ll.removeAtbeg()
    ll.removeAtpos(2)
    ll.removeAtEnd()
    
    
    ll.printList()
    
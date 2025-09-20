class stack :
    def __init__ (self):
        self.stack = []
        self.top = - 1 
        
    def push(self,arr):
        
        for i in range(len(arr))  :
            self.stack.append(arr[i])
            self.top +=1 
            
            
    def printStack(self):
        ptr = self.top
        
        for i in range (ptr , -1 , -1):
            print(self.stack[i])
        
    def reverse (self, arr):
        for i in range(len(arr)):
            arr[i]= self.stack.pop()
            self.top -= 1 
        print(arr)



if __name__ == "__main__":
    
    arr= [10,20,30,40,50,60]
    
    s = stack ()
    s.push(arr)
    s.printStack()
    s.reverse(arr)
    
    
    
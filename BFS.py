class BFSS:
    
    def __init__(self):
        self.rear=-1
        self.q=[None]*100
        self.front=-1
        
    
    def enqueue(self,data):
        
        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
        
        else:
            self.rear+=1
        
        self.q[self.rear]=data
        
    
    def printq(self):
        temp = self.front
        
        while temp <= self.rear:
            
            print(self.q[temp])
            temp+=1
        
        
    def deque(self):
        
        if self.rear==-1 or self.front>self.rear:
            print("Underflow")
            self.front=-1
            self,rear=-1
            return None
        
        else :
            item = self.q[self.front]
            self.front+=1
            
            
        return item 
            
        
        
    def dfs(self,n,start,data):
        visited = [0 for _ in range(n+1)]
        
        result=[]
        self.enqueue(start)
        visited[start]=1
        
        while self.front <= self.rear :
            e=self.deque()
            result.append(e)
            
            for i in data[e]:
                if visited[i]==0:
                    self.enqueue(i)
                    visited[i]=1

        
        print(visited)
        print(result)
starting_node = 1
n = 9 
data = [
    [],
    [2,8],
    [1,3,4],
    [2],
    [2,5],
    [4,6],
    [5,7],
    [6,8],
    [1,7,9],
    [8]
    ]
    
print(data)

q= BFSS()
q.dfs(n,starting_node,data)




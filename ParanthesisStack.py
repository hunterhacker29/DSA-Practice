class para:
    def __init__(self):
        self.stack = []
        self.top = -1 
        
    def checkPara(self, arr):
        for i in range(len(arr)):
            # Opening brackets
            if arr[i] == '(' or arr[i] == '[' or arr[i] == '{':
                self.top += 1
                self.stack.append(arr[i])
            
            # Closing brackets
            elif arr[i] == ')' or arr[i] == ']' or arr[i] == '}':
                if self.top == -1:
                    return False  # Extra closing bracket with no match
                
                if (self.stack[self.top] == '(' and arr[i] == ')') or \
                   (self.stack[self.top] == '[' and arr[i] == ']') or \
                   (self.stack[self.top] == '{' and arr[i] == '}'):
                    self.stack.pop()
                    self.top -= 1
                else:
                    return False  # Mismatched bracket
        
        # After loop, check if stack is empty
        if self.top == -1:
            return True
        else:
            return False
    
    def display(self):
        if self.top == -1:
            print("Stack is empty — Parentheses are in correct order ✅")
        else:
            print("Unmatched parentheses remain — Invalid string ❌")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

if __name__ == '__main__':
    arr = '{[()]}'
    print("Input:", arr)
    
    q = para()
    result = q.checkPara(arr)
    
    if result:
        print("String is Valid ✅")
    else:
        print("String is Invalid ❌")
    
    q.display()

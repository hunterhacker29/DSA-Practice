class post :
    def precedence(self,ch):
        if ch == '+' or ch == '-':
            return 1
        if ch == '*' or ch == '/':
            return 2
        if ch == '^' :
            return 3
        
        return 0 
            
    
    def intopos(self,arr):
        stack =[]
        result = []
        
        
        for i in arr :
            if ("a"<=i<="z") or ("A"<=i<="Z") or ("0"<=i<="9"):
                result.append(i)
                
            
            elif i == "(":
                stack.append(i)
            
            elif i == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                if stack and stack[-1] == "(":
                    stack.pop()
                
            
            else :
                while stack and self.precedence(i)<= self.precedence(stack[-1]):
                    result.append(stack.pop())
                
                stack.append(i)
        
        
        while stack :
            result.append(stack.pop())
        print("stakc is ",stack)
        print("Result is:", result)
        
        result = "".join(result)
        print("Result is:", result)

obj = post()

expr = "a+b*(c^d-e)"

print("Infix Expression: ", expr)
print("Postfix Expression: ", obj.intopos(expr))
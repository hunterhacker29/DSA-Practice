


num  =13
ans= ""

while num >0:
    if num % 2 == 0:
        ans+= '0'
    else:
        ans+='1'
        
    num = num //2 

print(ans[::-1])
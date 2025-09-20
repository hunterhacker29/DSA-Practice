data = {
    
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

ip = "MCMXCIV"
result = 0 
for i in range(len(ip)) :
    if i+1<len(ip) and data[ip[i]]<data[ip[i+1]]:
        result -=data[ip[i]]
    
    else :
        result += data[ip[i]]
            

print(result)
    
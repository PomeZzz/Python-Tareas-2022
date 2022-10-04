import math 
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un Numero: "))  
    
def hcf(a, b): 
    if(b == 0): 
        return a 
    else: 
        return hcf(b, a % b) 
  
    
print("el Mcd de a y b es : ", end="")    
print(math.gcd(a,b))
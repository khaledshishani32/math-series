
def fibonacci(n):
    if n == 0:
       return n
    elif n == 1:
        return n  
    else:
       return(fibonacci(n-1) + fibonacci(n-2))




def lucas(n) :
 

    a = 2
    b = 1
     
    if (n == 0) :
        return a
  
  
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
     
    return b
     
  

n = 7




def sum_series(n , n1=0 , n2=1):
    if(n > 1 and n1==0 and n2==1):
        return fibonacci(n)
    if(n >1 and n1==2 and n2==1):
        return lucas(n)
    else:
     if(n == 0 ):
         return n1
     if(n == 1):
       return n2
     else:    
       return sum_series(n-1 , n1 ,n2) + sum_series(n-2 , n1 ,n2)     
    

print("-----------------------")

print(sum_series(5,0,1))
print("-----------------------")
print(sum_series(7,2,1))
print("-----------------------")
print(sum_series(7, 5, 2))



# recursion 
# where a function calls itself

def fac(n):
           if n == 0:
                      return 1

           else: 
                      return n * fac(n-1)

n= 5
res = fac(n)
print(res)
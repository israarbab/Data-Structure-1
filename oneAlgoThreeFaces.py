def fun1(n):
  return n*(n+1)/2

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(1, i+1):
        sum += 1
    return sum
      
print("Time complexity of Fun1",fun1(4))   
print("Time complexity of Fun2",fun2(4))
print("Time complexity of Fun3",fun3(4))
  
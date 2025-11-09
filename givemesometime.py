def sum(n):
    return n*(n+1)/2

def arraySum(a):
    sum=0
    for i in a:
        sum = sum+i
    return(sum)

a=[12,3,4,15]
arraySum(a)

def summ(n):
    if(n<=0):
        return
    return n+summ(n-1)
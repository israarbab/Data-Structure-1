def prints(n):
    if(n<=0):
        return
    print("Codingal")
    n-=1
    prints(n/2)
    prints(n/2)

print(prints(7))
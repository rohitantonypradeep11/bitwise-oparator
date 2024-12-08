def abc(n):
    c = 0
    while n:
        c = c+1
        n >>=1
    return c
n = int(input("enter a number"))
print(abc(n))
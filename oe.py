def abc(n):
    if(n^1==n+1):
        return True
    else:
        return False
a = int(input("enter a number"))
if abc(a):
    print("its an even number")
else:
    print("its an odd number")
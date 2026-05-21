#### Alternative print
def fun7(*a):
    print("using slice")
    print(sum(a[::2]))
    print(a,"   Unpack:",*a,"  alternative:",*a[::2],end="\n")
    i=0
    s=0
    while i<len(a):
        if i%2==0:
            s+=a[i]
        i+=1
    print("using while loop")
    print(s)

fun7(1,7,8,25,30,60,70)
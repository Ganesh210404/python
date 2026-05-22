# def func(x,y):
#     print(x,y)
#     return x+y
# print(func(10,20))

# def great(a,b):
#     if a>b:
#         return a
#     else:
#         return b #executes 77
# print(great(75,77))
# --------------------------------------------------
def func(*a):
    s=sum(a)
    if s%2==0:
        return "even",s
    else:
        return "odd",s
print(*func(1,7,8,6,5,3,2,8))
# -----------------------------------------------------
def fun(*a):
    return sum(a)
x=fun(1,2,3,4,5,6,6)
if x%2==0:
    print(f"even : {x}")
else:
    print(f"odd : {x}")
# --------------------------------------------------------
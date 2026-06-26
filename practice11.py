# n=int(input("no of times checking: "))
# for i in range(1,n+1):
#     a=int(input('ENTER A NUMBER: '))
#     if(a%2==0):
#         print("even")
#     else:
#         print("odd")



# n=int(input())
# c=0
# for i in range(n-1,1,-1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         c=c+1
#         if c==1:
#             print(i)



# n=int(input())
# i=n+1
# while True:
#     fc=0
#     for j in range(1,i+1):
#         if i %j==0:
#             fc=fc+1
#     if fc==2:
#         print(i)
#         break
#     i=i+1





# n=int(input())
# l=n-1
# while l<n:
#     b=True
#     for i in range(2,int(l**0.5)+1):
#         if l%i==0:
#             b=False
#     if b==True:
#         dif=n-l
#         break
#     l=l-1
# h=n+1
# while h>n:
#     b=True
#     for i in range(2,int(h**0.5)+1):
#         if h%i==0:
#             b=False
#     if b==True:
#         dif1=h-n
#         break
#     h=h+1
# if dif<dif1:
#     print(l)
# if dif1<dif:
#     print(h)
# else:
#     print(l,h)


# n=int(input())
# s=int(input())
# r=int(input())
# for i in range(n):
#     gp=s*(r**i)
#     print(gp)


# n=int(input())
# for i in range(0,n):
#     if i<=1:
#         print(i,end=" ")
#     else:
#         print((i-1)+(i-2),end=" ")


# def mul(a,b,c):
#     return a*b*c
# print(mul(10,20,30))

# def calculator(a,b,operation):
#     def add():return a+b
#     def sub():return a-b
#     def mul():return a*b
#     def div():return a/b
#     def mod():return a%b
#     def floor():return a//b
#     if operation=='+':
#         print(add())
#     elif operation=='-':
#         print(sub())
#     elif operation=='*':
#         print(mul())
#     elif operation=='/':
#         print(div())
#     elif operation=='%':
#         print(mod())
#     elif operation=='//':
#         print(floor)()
# calculator(47,92,'+')

# def order(product, quantity=1, price=100):
#     print(product,quantity,price)
#     print(product, quantity, price)
# order("soap",40,338)
# order("soap",29)
# order(quantity=51,price=999,product="tea")

# def run_twice(func,value):
#     first=func(value)
#     return func(first)
# def double(x):
#     return x*2
# print(run_twice(double,3))
# double(6)
from functools import reduce
# l=[1,2,3,4,5]
# m=list(map(lambda x:x**3,l))
# f=list(filter(lambda x:x%2==0,m))
# r=reduce(lambda a,b:a+b,f)
# s=sorted(f,key=lambda x:x%2,reverse=False)
# print(m)
# print(f)
# print(r)
# print(s)
# s=sorted(list(filter(lambda x:x%2==0,list(map(lambda x:x**3,l)))),key=lambda x:x%2,reverse=False)
# print(s)

#
# w=["Ganesh","Yash","Ashish","ajay","lucky"]
# cap=list(filter(lambda w:w[0].isupper(),w))
# print(cap)



# p=[("Ganesh",21),("Ajay",22),("Ashish",20),("Yas",23)]
# sp=list(sorted(p,key=lambda p:p[1]))
# print(sp)



# def my_map(func,lst):
#     res=[]
#     for i in lst:
#         res.append(func(i))
#     return res
# print(my_map(lambda x:x*2,[1,2,3]))



# def apply_operation(a,b,op):
#     return op(a,b)
# add=lambda x,y:x+y
# sub=lambda x,y:x-y
# mul=lambda x,y:x*y
# print(apply_operation(20,10,add))
# print(apply_operation(20,10,sub))
# print(apply_operation(20,10,mul))


# n=range(1,21)
# mul_of_3=filter(lambda x:x%3==0,n)
# sq=list(map(lambda x:x**2,mul_of_3))
# print(sq)



# students = [ {'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 45}, {'name': 'Carol', 'score': 72}, {'name': 'Dave', 'score': 90}, ]
# passing = filter(lambda s: s['score'] >= 60, students)
# def add_grade(s):
#     return {**s, 'grade': 'Pass'}
# graded = map(add_grade, passing)
# final = sorted(graded, key=lambda s: s['score'], reverse=True)
# for s in final: print(s)


# def p(a):
#     fc=0
#     for i in range(1,a+1):
#         if a%i==0:
#             fc+=1
#     return fc==2
# n=int(input())
# ap=n+1
# bp=n-1
# while True:
#     if p(ap):
#         print(ap)
#         break
#     ap+=1
# while(bp>=2):
#     if p(bp):
#         print(bp)
#         break
#     bp-=1
#
#123
#
# 123
# 312
# 231
# use n=123 and print circular of this number's digits example for this n=123 the output should 123,312,231

n=112
t=n
dc=0
rot=[]
while t>0:
    dc=dc+1
    t=t//10
t=n
for i in range(1,dc+1):
    print(t)
    rot.append(t)
    r=t%10
    t=t//10
    t=r*(10**(dc-1))+t
print(rot)
for i in rot:
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc=fc+1
    if fc==2:
        print("Prime number is",i)
# n1=int(input("n1: "))
# n2=int(input("n2: "))
# h=min(n1,n2)
# l=min(n1,n2)
# #gcd
# for i in range(l,0,-1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
#         break
# k=h
# while True:
#     if h%n1==0 and h%n2==0:
#         lcm=h
#         break
#     h=h+k
# print(lcm,gcd)

# n=int(input("enter: "))
# c=0
# t=n
# s=0
# while t>0:
#     r=t%10
#     p=r
#     fc=0
#     for i in range(1,p+1):
#         if p%i==0:
#             fc+=1
#     if fc==2:
#         s=s+p
#     t=t//10
# print(s)

# *
# * *
# * * *
# * * * *
# * * * * *
#
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         # if i>=j:
#         print("*",end=" ")
#     print()


#     *
#    **
#   ***
#  ****
# *****
# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")  or print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print("*",end="")   --> if we give end=" " it'll print equalateral triangle
#             or
#         print("*"*i)
#     print()


# * * * * *
# * * * *
# * * *
# * *
# *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(end=" *")
#     # for j in range(1,i+1):
#     #     print("*",end="")
#     print()







# *****
#  ****
#   ***
#    **
#     *
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(end=" ")
#     for j in range(1,n-i+2):
#         # if i>=j:
#         print("*",end="")
#     print()
# n=int(input())
# s=0
# for i in range(n+1):
#     s=s+i
# print(s)



# s=int(input("enter start range: "))
# e=int(input("enter end range  : "))
# print(f"even numbers between {s} and {e} are:",end=" ")
# for i in range(s,e+1):
#     if i%2!=0:
#         print(i,end=" ")


#
# n=int(input())
# for i in range(1,11):
#     print(n*i,end=" ")

# s=int(input())
# e=int(input())
# if s<=0 or e<=0:
#     print("Invalid Inputs")
# else:
#     c=0
#     for i in range(s+1,e):
#         if i%2==0:
#             c+=1
#             if c%2!=0:
#                 print(i,end=" ")

l=[[1,2],[3,4],[5,6]]
r=list(map(lambda x:x+[5],l))
print(l)
print(r)
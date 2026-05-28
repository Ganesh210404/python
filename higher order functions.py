#Maps
# l=[[1,2],[3,4],[5,6]]
# r=list(map(lambda x:x+[5],l))
# print(l)
# print(r)

# l=[1,2,3,4,5,6,7,8]
# e=list(filter(lambda x:x%2,l))
# print(e)

# l=[3,6,1,2,5,9,12,16]
# e=list(filter(lambda x:x%3,l))
# print(e)

a=input()
# s=a.split(",")
# l=['a','e','i','o','u','A','I','O','U']
l="AEIOUaeiou"
e=list(filter(lambda x:x not in l,a))
print(e)
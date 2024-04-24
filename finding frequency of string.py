x=input("enter string")
print(x)

result=dict((i,x.count(i)) for i in x)
print((result))
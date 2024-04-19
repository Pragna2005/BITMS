apple=[10,5,30,40,50]
print(apple)
print(apple[0])
print(apple[1])
print(apple[2])
print(apple[-1])
print(apple[-3])
print(apple[-2])
print("elements of apple")
for i in apple:
    print(i)
apple[1]=100
print(apple)
apple[2]=(300,400)
print(apple[-1])
apple[3]=500,600,700
print(apple)
apple[0:3]=(-10,-20,-30,-40,-50,-60)
print(apple)
a=(100,200,300,(3,4,5),800,("hi","tc"))
print(a[5][1])

b=(50,40,20,10,30,60,70,100,90,80)
print(type(b))
print(b[3:12])
print(b[-5:-3])

a=(10,20,30,40,50)
print(a*2)  #duplication

a=(90,100,70,-10,20)
print(len(a),end='$')
print(max(a),end='$')
print(sum(a),end='$')
print(sum(a)//len(a))


a=(10,20,30,(100,200,400),40,50)
print(a+(90,50))  #concatenate


c=(100,200,300,("hi","hlo","bye"),(10.5,12.5,30.5))
print(c[-1][-1])

age=[10,20,[30,40,[50,60],70],80,"hi",True]
print(age[2][2][1])  #to print 60
print(age[5])

a=10
print(type(a))

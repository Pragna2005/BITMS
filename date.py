date=int(input("enter date"))
month=int(input("enter month"))
'''if month<13:
    print(month)
else:
    print('invalid')
'''    
# if month<13:
year=int(input("enter year"))
c=year//100
d=year%100
month=month-2
f=date+((13*month-1)/5)+d+(d/4)+(c/4)-2*c
fres=int(f%7)
day={0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thurs',5:'fri',6:'sat'}
print(fres)
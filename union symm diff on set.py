'''days1={'mon','tue','wed','thurs','sun'}
days2={'fri','sat','sun'}
print(days1|days2)    #or oper -->doesnt print repeated ones


days1={'mon','tue','wed','thurs','sun'}
days2={'fri','sat','sun'}
print(days1.union(days2)) #using union same like or


s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
q=s1.union(s2,s3)     #doesnt repeat elements
print(q)
c=(s1.intersection(s2,s3))
print(c)

days1={'mon','tue','wed','thurs'}
days2={'mon','tue','sun'}
print(days2-days1)

days1={'mon','tue','wed','thurs'}
days2={'mon','tue','sun'}
print(days1.difference(days2))'''


'''a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b   #common elements r eliminated
print(c)'''

a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a.symmetric_difference(b)
print(c)

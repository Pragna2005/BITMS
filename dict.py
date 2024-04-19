emp={"name":"prag","age":18,"sal":200000,"dob":"2000-15-15"}
print(emp)
print(emp.keys())
print(emp.items())
del emp["name"]
print(emp)
pop_key=emp.pop("age")
print(pop_key)
print(sorted(emp))#sorts in alphabetical order

Dict=dict({1:"poo",2:"prag",3:"aksh"})
print(Dict)

Dict=dict([(4,'poo'),(2,'sindhoo')]) #([-->tuple ,converting tuple to dict
print(Dict)
print(type(Dict))

Dict[0]='tom'
Dict[2]='jerry'
Dict[3]='pooh'
print(Dict)

Dict['age']=12,3,22
print(Dict)




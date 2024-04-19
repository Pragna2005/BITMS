#set method
'''states={"karnataka","goa","TN","AP"}
print(states)
print(type(states))
print("looping through set ele")
for i in states:
    print(i)'''

#set is immutable(cant access ele by index),set is unordered,removes duplicate values
'''set={10,20,50,40,60,10,100,90,30}
print(set)'''

districts=set(["ooty","bly","bng","chennai","kovai"])
print("\nprinting original set")
districts.add("hpt");
'''for i in districts:'''
print(districts)
districts.discard("bly")
print(districts)
districts.remove("ooty")
print(districts)
districts.discard("ooty")    #doesnt show error even if element is not present
print(districts)
'''districts.remove("ooty")'''      #shows error if ele is not in set
print(districts)
districts.pop()
print(districts)
districts.clear()     #clears all elements
print(districts)

    
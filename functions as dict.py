def prag(a,b):
    print(a+b)
test_dict={"fname":prag,"age":18,"address":"bly"}
print("the original dictionary is :"+str(test_dict))

test_dict['fname'](10,20)
# print("the req call result :"+int(res))
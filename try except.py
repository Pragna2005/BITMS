'''try:
    num=10
    deno=0
    result=num/deno
    print(result)
except:
    print("error:denominator cant be 0")
    
prag=5/0
print(prag)'''

'''try:
    even_num=[2,4,6,8]
    print(even_num[2]/0)
except ZeroDivisionError:
    print("division cant be 0")
except IndexError:
    print("index out of bound")'''

'''try:
    num=int(input("enter no"))
    assert num%2==0
except:
    print("not an even num!")
else:
    reciprocal=1/num
    print(reciprocal)'''

try:
    num=10
    deno=0
    result=num/deno
except:
    print("denominator cant be 0")
finally:
    print("this is finally block")
    
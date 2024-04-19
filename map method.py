'''x,y=map(int,input().split())
print(x)
print(y)

x,y=[int(x) for x in input().split()]
print(x)
print(y)'''

'''nums=[10,20,30,40,50]
double=[num*2 for num in nums]
print(double)

nums=[10,20,30,40,50]
sq_nums=[]
#for loop to square each element
for num in nums:
    sq_nums.append(num*num)
print(sq_nums)

nums=[10,20,30,40,50]
sq=[num*num for num in nums]
print(sq)'''

#conditionals in list comprehension
#expn for item in list if cond==TRUE
#filtering even numbers from a list
'''even=[num for num in range(1,30) if num%2==0]
print(even)'''

name='pragna'
vowels='aeiou'
vowel=[char for char in name if char in vowels]
print(vowel)
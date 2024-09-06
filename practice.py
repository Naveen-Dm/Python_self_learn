'''# print even numbers
n = int(input("enter no: "))
val = 2
for i in range(n):
    print(val, end = " ")
    val += 2'''

'''# print odd numbers
n = int(input("enter no: "))
val = 1
for i in range(n):
    print(val, end = " ")
    val += 2'''

'''# factorial number
# ex: 5 = 5*4*3*2*1 = 120
n = int(input("enter no: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)'''

'''# sum of n naturals number
# ex: 5 = 5+4+3+2+1 = 15
n = int(input("enter no: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)'''

'''# sum of elements in list
l1 = [1,2,3,4,5]
sum = 0
for i in l1:
    sum = sum + i
print(sum)'''

'''# find odd and even in given list
l1 = [1,2,3,4,5,6,7,8,9,10,0]
even = 0
odd = 0
z = 0
for i in l1:
    if i == 0:
        z += 1
    elif i % 2 == 0:
        even += 1
    else: 
        odd += 1
print(even,odd,z)'''

'''# find count of negative number in a list
l1 = [1,2,3,-4,-5,6,-7,8,9,10,0]
c = 0
for i in l1:
    if i < 0:
        c += 1
print(c)'''

'''# how many elements are repeating in a list
l1 = [1,2,3,4,3,2,5,6,7]

n = int(input("enter no: "))
c = 0
for i in l1:
    if i == n:
        c +=1
print(c)'''

'''# find min and max in given list
l1 = [2,3,4,5,3,455,5,433,4,5,54]

min = l1[0]
max = l1[0]
for i in l1:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)'''

'''# count no of spaces in given string
s1 = "Hi my name is naveen"

c = 0
for i in s1:
    if i == " ":
        c += 1
print(c)'''

'''# find length of string
s1 = "Hi my name is naveen"

c = 0
for i in s1:
    c += 1
print(c)'''

'''# find number of vowels
s1 = "Hi my name is naveen"

c = 0
s2 = s1.lower()
for i in s2:
    if i in "aeiou":
        c += 1
print(c)'''

'''# count no of numbers in string
s1 = "Hi my name is naveen00123"

c = 0
s2 = s1.lower()
for i in s2:
    if i in "0987654321":
        c += 1
print(c)'''

n = 6
n1 = 0
n2 = 1
for i in range(0, n):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
# print(n3) 



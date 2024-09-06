# n1 = 10
# n2 = 20
# sum = n1 + n2
# print(sum)

#1# to find sqrt of nmbr
# n1 = 5
# sr = n1**(0.5)
# print(sr)

#2# area of triangle
# height = float(input("enter the height: "))
# base = float(input("enter the base: "))
# area = (1/2) * base * height
# print(area)

#3# swap 2 nmbrs
# n1 = 10
# n2 = 20

# temp = n1
# n1 = n2
# n2 = temp

# print(n1)
# print(n2)

#4# swap 3 nmbrs
# n1 = 10
# n2 = 20
# n3 = 30

# temp = n3
# n3 = n2
# n2 = n1
# n1 = temp

# print(n1)
# print(n2)
# print(n3)

#5# program to check entered nmbr is positivie or negative

# n = -0.1

# if n > 0:
#     print("positive")
# elif n == 0:
#     print("number is zero")
# else:
#     print("negative")

#6# largest of 3 nmbrs
# n1 = 1
# n2 = -10
# n3 = 80


# if (n1 > n2) and (n1 > n3):
#     print("n1 is greater")
# elif (n2 > n1) and (n2 > n3):
#     print("n2 is greater")
# else:
#     print("n3 is greater")

#7# prime or not 
# n = 12

# if n == 1:
#     print("not prime")

# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("no")
#             break
#     else:
#         print("yes")

#8# print all prime nmbrs

# low = 2
# high = 50

# for n in range(low, high + 1):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)

#9# factorial of nmbr
# n = 5

# fact = 1

# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

#10# display the multiplication tables

# n = 7
# n1 = 10

# for i in range(1, n1 + 1):
#     print(n, "x" , i, "=", n*i)

#11# fibonacci series
# n = 7
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
# for i in range(0, n):
#     fib = n1 + n2
#     n1 = n2
#     n2 = fib

#     print(fib)


#12# Python program to check if the number is an Armstrong number or not

# take input from the use
# num = int(input("Enter a number: "))
# sum = 0

# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** len(str(num))
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:   
#    print(num,"is not an Armstrong number")

# s = "neevan si a doog yob"
# l=[]
# s1=""
# for i in s:
#     if i==" ":
#         l.append(s1)
#         s1=""
#     else:
#         s1=i+s1
# if len(s1)>0:
#     l.append(s1)
# print(l)

#13# Number divisible by another number
# l = [39,48,26,98,33,67,87]
# l1 = []
# for i in l:
#     if i % 13 == 0:
#         l1.append(i)
#         print(l1)
#         # print(i)


#14# mini calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division \n")

# choice = int(input("enter your choice from 1-4: "))

# if choice == 1:
#     print(num1 + num2)
# elif choice == 2:
#     print(num1 - num2)
# elif choice == 3:
#     print(num1 * num2)
# elif choice == 4:
#     print(num1 / num2)
# else:
#     print("Invalid")

#15# 
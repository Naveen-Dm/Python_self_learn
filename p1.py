# n=int(input("please enter a number between 1 to 12:\n"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
# fib=[0,1]
# n=6
# for i in range(n-2):
#     c=fib[-1]+fib[-2]
#     fib.append(c)
# print(fib)


# class metro1:
#     def __init__(self,toy,cloth):
#         self.toy=toy
#         self.cloth=cloth
#     def metro1(self):
#         print(f"metro items are {self.toy} and {self.cloth}")
# class metro2:
#     def __init__(self,veg,fruit):
#         self.veg=veg
#         self.fruit=fruit
#     def metro2(self):
#         print(f"metro items are {self.veg} and {self.fruit}")
# class metro(metro1,metro2):
#     def __init__(self, toy, cloth,veg,fruit):
#         metro1.__init__(self,toy, cloth)
#         metro2.__init__(self,veg,fruit)
#     def metro(self):
#         print(f"metro items are {self.toy},{self.cloth},{self.fruit},{self.veg},")
# items=metro("as","asas","dsfdsf","efwefw")
# items.metro1()
# items.metro2()
# items.metro()
# c=metro1("assss","sdaas")

# s = "How are you"
# v="aeiou"
# s = list(s)
# i=0
# j=len(s)-1
# while i<j:
#     while i<len(s):
#         if s[i] not in v:
#             i+=1
#         else:
#             break
#     while j>0:
#         if s[j] not in v:
#             j-=1
#         else:
#             break
#     if i<j:
#         s[i],s[j]=s[j],s[i]
#         i+=1
#         j-=1
# print("".join(s))


# Python program to check if the number is an Armstrong number or not

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


# class RawAgent:
#     def __init__(self,name,number):
#         self.__name=name
#         self.__number=number

#     def getName(self):
#         return self.__name
#     def getNumber(self):
#         return self.__number
#     def setName(self,name):
#         self.__name=name
#     def setNumber(self,number):
#         self.__number=number
# afan=RawAgent("afan",3562)
# # print(afan)
# # print(afan._RawAgent__name)
# print(afan.getName())
# print(afan.getNumber())
# afan.setName("afan123")
# afan.setNumber(1234)
# print(afan.getName())
# print(afan.getNumber())
# afan._RawAgent__name="awadh"

# l=[2,5,3,7,4]
# target=10


# d={}
# for i in range(len(l)):
#     remainder=target-l[i]
#     if remainder in d:
#         print(d[remainder],i)
#         break
#     d[l[i]]=i
# else:
#     print(-1)
# for i in range(len(l)//2+1):
#     remainder=target-l[i]
#     if remainder in l:
#         print(l[i],remainder)
# from collections import Counter
# l=[2,5,3,7,4]
# d=Counter(l)
# print(d)
# l=["H"]*5
# k=1
# i=1
# l[0]="T"
# while k<len(l):
#     if i%k==0:
#         if l[i]=="H":
#             l[i]="T"
#         else:
#             l[i]="H"
#     print(l)
#     i+=1
#     if i==len(l):
#         print("______________")
#         k+=1
#         print(k)
#         i=1
    
# k=1
# j=0
# while k<len(l):
#     for i in range(j,len(l)):
#         if i%k==0:
#             if l[i]=="H":
#                 l[i]="T"
#             else:
#                 l[i]="H"
#     print(l)
#     k+=1
#     j+=1
# t=(2,4,5,[56,8])
# t[-1].append(4)
# print(t)

# s="qwertyuiop"
# l=s.split("")
# print(s[9:])

# s,t=set((3,4,5)),set("sdfsdfsd"),{"a":1}
# print(s,type(s),t,type(t))
# s={2,4,5,6}
# x=range(10)
# print(type(x))

# l=["H"]*6
# k=0

# while k<len(l):
#     for i in range(k,len(l),k+1):
#         if l[i]=="H":
#             l[i]="T"
#         else:
#             l[i]="H"
#     k+=1
#     print(l)
# print(l)

# l= ["MrArhanafan1","Mrarjunafan1", "MrAmir"]

# res=""
# for i in l[0]:
#     print(res+i," ------ ",i)
#     print(l[1].find((res+i)))
#     if l[1].find((res+i))!=-1:
#         res+=i 
# print(res)
# test_list = [1, 4, 5, 7, 8]
 
# # Printing test_list
# print("The list is : " + str(test_list))

# s= "We can delete the file in Python using the os module The remove function of the os module is used to delete a file in Python by passing the filename as a parameter"
# l=s.split(" ")
# d={}
# i=0
# j=len(l)-1
# while i<j:
#     if d.get(l[i]):
#         if type(d.get(l[i]))==list:
#             d[l[i]].append(l[j])
#         else:
#             d[l[i]]=[d[l[i]],l[j]]
#         # d[l[i]].append(l[j])
#     else:
#         d[l[i]]=l[j]
#     i+=1
#     j-=1
# print(d)

# l=[190,50,10,25,6,95,105,0,-1,-10,100]
# lmax=[]
# lmin=[]
# maxi=-1000000
# mini=10000000

# l= [1, 6, 3, 5, 3, 4,-1]
# c=0;c1=0
# for i in l:
#     if i>c:
#         c1=c
#         c=i
#     else:
#         if c1<i:
#             c1=i
# print(c)
# print(c1)

# s="mega#@is#@a#@good#@boy"
# res=""
# r=""
# for i in s:
#     if ord(i) in range(ord("a"),ord("z")+1):
#         r=i+r
#     else:
#         res=res+r+i
#         r=""
# # print(res)
# if len(r)>0:
#     res=res+r
# print(res)



# agem si a doog yob
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


# s="meganath"
# k=3
# r=""
# res=""
# c=0
# for i in range(0,len(s),k):
#     st=s[i:i+k]
#     if c%2==0:
#         res=res+st[::-1]
#     else:
#         res+=st
#     c+=1
# print(res)
    
# s="meganath"
# print(type(s[0:0]))
# k=3
# res=""
# r=""
# for i in range(len(s)):
#     if i<k and i>=0:
#         res+=s[i]
#     elif i>=len(s)-k:
#         res=res+r
#         res+=s[i]
#         r=""
#     else:
#         r=s[i]+r
# print(res)
# s="meganatha"
# r=s.__iter__()
# print(next(r),r)
# print(next(r),r)
# print(next(r),r)
# print(next(r),r)
# print(next(r),r)
# print(next(r),r)
# print(next(r),r)
# print(next(r),r)

# n=5
# for i in range(n+1):
#     print(" "*(n-i),"* "*i)

# l=[-1,4,5,-6,6]
# mx=l[0]
# for i in range(len(l)):
#     num=sum(l[i:])
#     if num>mx:
#         mx=num
# print(num)


# l=[1,2,3,4,5,6,7]
# d=[]
# for i in l:
#     d.insert(0,i)
# print(d)
# c=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         c+=1
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(c)
# k=0
# i=0
# j=1
# while True:
#     k+=1
#     if l[i]>l[j]:
#         l[i],l[j]=l[j],l[i]
#         i-=1
#         j-=1
#         if i<0:
#             i=0
#             j=1
#     else:
#         i+=1
#         j+=1
#     if j==len(l):
#         break
# print(k)


# list_a = [1, 2, 3, 4,5] 
# list_b = [4, 5, 6, 7, 8]
# l=[ i for i in list_a if i in list_b]
# for i in list_a:
#     if i in list_b:
#         l.append(i)
# print(l)

# def o_e(*n):
#     print(len(n))    
# o_e(19,20,34,8)

# def num():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# n=num()
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))


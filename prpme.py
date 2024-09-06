# import calendar
# import datetime
# import datetime
# for i in range(2000,3000):
#     j=1
#     while j<=12:
#         date_string = f"{i}-{j}-1"
#         year, month,day= map(int, date_string.split("-"))
#         num_days = calendar.monthrange(year, month)[1]
#         # print(type(num_days))

#         last_day=datetime.datetime(year,month,num_days)
#         if last_day.strftime('%A')=='Saturday':
#             last_working_day=num_days-1
#         elif last_day.strftime('%A')=='Sunday':
#             last_working_day=num_days-2
#         else:
#             last_working_day=num_days
#         print(f"Number of days in {calendar.month_name[month]} {year}: {num_days} and last day : {last_day.strftime('%A')} and last working date : {last_working_day}")
#         j+=1
        
# def last_two_working_days(year,mon):
#     years={}
#     for i in year:
#         months={}
#         for j in mon:
#             date_string = f"{i}-{j}-1"
#             year, month,day= map(int, date_string.split("-"))
#             num_days = calendar.monthrange(year, month)[1]
#             last_day=datetime.datetime(year,month,num_days)
#             if last_day.strftime('%A')=='Saturday':
#                 last_working_day=num_days-1
#             elif last_day.strftime('%A')=='Sunday':
#                 last_working_day=num_days-2
#             else:
#                 last_working_day=num_days
#             if last_day.strftime('%A')=='Monday':
#                 dates=(f"{year}-{month}-{last_working_day-3}",f"{year}-{month}-{last_working_day}")
#             else:
#                 dates=(f"{year}-{month}-{last_working_day-1}",f"{year}-{month}-{last_working_day}")
#             months[j]=dates
#             # print(months)
#             # print(dates)
#             # print(f"Number of days in {calendar.month_name[month]} {year}: {num_days} and last day : {last_day.strftime('%A')} and last working date : {last_working_day}")
#         years[i]=months
#     return years
# data=last_two_working_days([2024,2025],[9,10,11])
# print(data)
# {2040:{4:(2040-04-30,2040-04-31),5:(2040-05-30,2040-05-31)},2050:{4:(2050-04-28,2050-04-29),5:(2050-05-30,2050-05-31)}}
# "2021-03-19"

# class Movie:
#     def __init__(self,name,typee,hour):
#         self.name=name
#         self.type=typee
#         self.hour=hour
#     def movie_info(self):
#         print('movie name-> ', self.name)
#         print('movi type-> ', self.type)
#         print('movie length-> ', self.hour)
# m1=Movie('battleship','action',2)
# m1.movie_info()

# class myclass:
#     x=200
#     def __init__(self):
#         self.a=10
#         self._b=20
#         self.__c=30
#     def display(self):
#         print(self.a)
#         print(self._b)
#         print(self.__c)
# m1=myclass()
# m1.display()
# print(m1.a)
# print(m1._b)
# print(m1._myclass__c)
# print(m1.__dict__)
# class RawAgent:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def getName(self):
#         return self.__name
#     def getAge(self):
#         return(self.__age)
#     def setName(self,name):
#         self.__name=name
#     def setAge(self,age):
#         self.__age=age
# rav=RawAgent('mubbu',25)
# print(rav.getAge())
# print(rav.getName())
# rav.setAge(30)
# rav.setName('affu')
# print(rav.getAge())
# print(rav.getName())

# class Company:
#     def __init__(self,companyName):
#         self.companyName=companyName
#     def slogan(self):
#         print("Organization is msys")
# class Project(Company):
#     def __init__(self,projectName,companyName):
#         super().__init__(companyName)
#         self.projectName=projectName
# class Employee(Project):
#     def __init__(self,name,projectName,companyName):
#         super().__init__(projectName,companyName)
#         self.name=name
#     def EName(self):
#         print(self.name)
#         self.slogan()
# mub=Employee('mubashir','hpe','msys')
# print(mub.companyName)
# print(mub.projectName)
# print(mub.name)
# mub.EName

# class MetroSale:
#     def __init__(self,toys,cloths):
#         self.toys=toys
#         self.cloths=cloths
#     def metroItems(self):
#         print(f'items in the metro are {self.toys} and {self.cloths}')

# class Dmart:
#     def __init__(self,pants,shirts):
#         self.pants=pants
#         self.shirts=shirts
#         self.a=10
#     def DmartItems(self):
#         print(f'items in the Dmart are {self.pants} and {self.shirts}')

# class BlinkIt(MetroSale,Dmart):
#     def __init__(self,toys,cloths,pants,shirts):
#         MetroSale.__init__(self,toys,cloths)
#         Dmart.__init__(self,pants,shirts)

# items=BlinkIt("watergun","reymonds","b","t")
# items.metroItems()
# items.DmartItems()
# print(items.a)
# class Heart:
#     def __init__(self,hb):
#         self.hb=hb
        
#     def analysis(self):
#         if self.hb<68 and self.hb>72:
#             print("abnormal")
#         else:
#             print('normal')
# class Patient:
#     def __init__(self,name,age,gender,hb):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.hb=hb
#         self.ob=Heart(self.hb)
# afan=Patient('afan',25,'M',72)
# print(afan.ob.__dict__)
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def fromBirthYear(cls,name,year):
#         cls(name, 2024 - year)
    
#     @staticmethod
#     def adult(age):
#         return age>18
# mub=Person('afan',25)
# print(mub.__dict__)
# mub2=Person.fromBirthYear('mub',2000)
# print(mub2.age)
# suhas=("1",("4",),["2"])
# print(suhas)

# suhas[-1].clear()
# print(suhas)
# suhas={20,40,60,29,30,"3"}
# afan={20,30,10,9,4}
# print(suhas.difference("3"))
# print(afan.difference(afan))
# d={1:20,2:30,3:35,4:50}
# d1=d
# d1=d.fromkeys([1,2,10],21)
# d1.update({1:100})
# print(d is d1)
# print(d1)
# k=d.items()
# print(type(k),k)
# a=0
# b=1
# for i in range(8):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
# num=10028956
# o=0
# e=0
# while num>0:
#     print(num)
#     r=num%10
#     if r==0:
#         pass
#     elif r%2==0:
#         e+=1
#     else:
#         o+=1
#     num//=10
# print(o,e)
# f=1
# for i in range(2,6):
#     f=f*i
# print(f)
# n=7
# b=0
# base=0
# while n>0:
#     rem=n%2
#     b=b+rem*base
#     base*=10
#     n//=2
# print(b)
# n=11
# for i in range(2,n//2+1):
#     if n%i==0:
#         print('not a prime number')
#         break
# else:
#     print("prime number")

# n=145
# temp=n
# sum=0
# def fact(n):
#     sum=1
#     for i in range(2,n+1):
#         sum*=i
#     return sum
# while temp>0:
#     r=temp%10
#     sum+=fact(r)
#     temp//=10
# print(n,sum)

# s='11431'
# max=0
# k=1
# for i in range(len(s)):
#     if int(s[i])==k:
#         r=int(s[0:i]+s[i+1:len(s)])
#         max=r if r>max else max
# print(max)

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# l=list(d.items())
# l.sort(key=lambda a:a[-1],reverse=True)
# print(d)
# print(l)
# print(dict(l))
# l=[11,3,6,7,2,2,5,5,6,6,7,4]
# d={}
# for i in l:
#     if d.get(i,0):
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# v="aeiou"
# rv=""
# s="hll"
# ns=""
# for i in s:
#     if i in v:
#         rv+=i
# r=rv[::-1]
# print(r)

# k=0
# for i in s:
#     if i in v:
#         ns+=r[k]
#         k+=1
#     else:
#         ns=ns+i

# print(ns)

N1 = "65661"
N2 = "6"
max=0
for i in range(len(N1)):
    if N1[i]==N2:
        m=int(N1[0:i]+N1[i+1:len(N1)])
        if m>max:
            max=m
print(max)

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
# print(afan.getName())
# print(afan.getNumber())
# afan.setName("afan123")
# afan.setNumber(1234)
# print(afan.getName())
# print(afan.getNumber())
# class Area:
#     def area(self):
#         pass

# class Rectangle(Area):
#     def area(self,l,b):
#         print(l*b)
# class Square(Area):
#     def area(self,s):
#         print(s**2)
# rec=Rectangle()
# rec.area(7,8)
# squ=Square()
# squ.area(4)

# s = "hello"
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

# s = "hello"
# v="aeiou"
# s = list(s)
# i=0
# j=len(s)-1
# while i<j:
#     while i<len(s):
#         if s[i] in v:
#             break
#         else:
#             i+=1
#     while j>0:
#         if s[j] in v:
#             break
#         else:
#             j-=1
    
# print("".join(s))

# def fact(a):
#     print(a)
#     if a==1:
#         return a
#     else:
#         return fact(a-1)*a
# print(fact(5))

# class metro1:
#     def __init__(self,toy,cloth):
#         self.toy=toy
#         self.cloth=cloth
#     def metroI(self):
#         print(f"metro items are {self.toy} and {self.cloth}")
# class metro2:
#     def __init__(self,veg,fruit):
#         self.veg=veg
#         self.fruit=fruit
# class metro(metro1,metro2):
#     def __init__(self, toy, cloth,veg,fruit):
#         metro1.__init__(self,toy, cloth)
#         metro2.__init__(self,veg,fruit)
#     def metroI(self):
#         print(f"metro items are {self.toy},{self.cloth},{self.fruit},{self.veg},")
# items=metro("as","asas","dsfdsf","efwefw")
# items.metroI()
# import random
# print(random.shuffle("afan"))


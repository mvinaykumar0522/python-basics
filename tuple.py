# #tuple is a collection datatypes,which is used to store the multiple values in a single variable 
# #tuple is orderd,imuteable,also allows the duplicate values and can store mixed data type in a values.
# #example:
# # coordinates=("x","y")
# # my_tuple=(10,20,30)
# # print(my_tuple)
# # print(type(my_tuple))
# #crrdeating a tuple 
# #empty tuple 
# # Et=()
# #tuple with numbers:
# # N=(1,2,3,4,5,6)
# #tuple with strings:
# # s=("a","b","c","A","B","C")
# #tuple with mixed datatypes
# # m=(24,3,14,"A","C",True,"False")
# #tuple with single elements:
# # a=10#int
# # b=[10]#list
# # c=(10,)#tuple 
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # my_tuple=(10,20,30)
# # print(my_tuple)
# # print(type(my_tuple))
# # #accessing elements 
# # print(my_tuple[0])#10
# # print(my_tuple[1])#20   
# # print(my_tuple[2])#30
# # print(my_tuple[-1])#30
# # print(my_tuple[-2])#20
# # print(my_tuple[-3])#10
# # #slicing of tuple
# # print(my_tuple[0:2])#(10,20)
# # print(my_tuple[1:3])#(20,30)
# # print(my_tuple[:2])#(10,20)
# # print(my_tuple[1:])#(20,30)
# # print(my_tuple[:])#(10,20,30)
# # #count()
# # my_tuple=(10,20,30,10,20,10)    
# # print(my_tuple.count(10))#3
# # print(my_tuple.count(20))#2
# # print(my_tuple.count(30))#1
# # print(my_tuple.count(10))#0\
# #changing the tuple values
# #tuples are immutable datatypes,so we cannot change the values 
# # a[i]=50
# # print(a)#type error:'tuple' object doesnt support item assigment 
# # #append():
# # a.append(50)
# # print(a)
# #length of a tuple
# # a=(10,20,30,40,50)
# # print(len(a))#5
# #maxmaximum value in a tuple
# print(max(a))#50
# #minimum value in a tuple
# print(min(a))#10
# #sum of a tuple
# print(sum(a))#150
# #concatenation of a tuple
# b=(60,70,80)
# c=a+b
# print(c)#(10,20,30,40,50,60,70,80)
# #repetition of a tuple
# d=a*2
# print(d)#(10,20,30,40,50,10,20,30,40,50)
# # searching and checking 
# print(10 in a)#True
# print(100 in a)#False
# #set of a tuple
# my_tuple=(10,20,30,10,20,30)
# print(set(my_tuple))#{10,20,30}
# #in operator
# print(10 in my_tuple)#True
# print(100 in my_tuple)#False
# #not in operator
# print(10 not in my_tuple)#False
# print(100 not in my_tuple)#True
# #index()
# my_tuple=(10,20,30,10,20,30)
# print(my_tuple.index(10))#0
# print(my_tuple.index(20))#1
# print(my_tuple.index(30))#2
# # sorting and reversing a tuple
# my_tuple=(30,10,20,50,40)
# print(sorted(my_tuple))#[10,20,30,40,50]
# print(tuple(reversed(my_tuple)))#(40,50,20,10,30)
# print(my_tuple[::-1])#(40,50,20,10,30)

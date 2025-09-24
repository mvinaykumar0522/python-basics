#collection data types:
#the collection data types is also called as non-primitive data types
#this collection of data is used to store multiple items in a single variable
#types of cdt:
#list
#tuple
#set
#dictionary
#lists in python:
#       lists are used to store multiple items in a single variable
#lists are collection data type which are used to store multiple items in a single variable
#lists are muteable(we can change,add or remove items from the list) data types and ordered(items have a fixed positions )
#example:
#fruits=["apple","banana","cherry"]#list of strings
#list1=[10,20,30,40,50]#list of integers
#list2=[10.1,20.2,30.3]#list of floats
#list3=[True,False,True]#list of boolean values
#list4=["apple",10,20.5,True]#list of mixed data types
#output:
#print(list4)
#accessing elements from a list:
#accessing elements are used to retrive the list items or values stored at a position (index-it starts from 0)
#index- in python,every element in a list is stored with a position number called index
#example: 0  1  2  3  4 . . . n-1
#list1=[10,20,30,40,50]
#print(list1[0])
#print(list1[1])
#print(list1[2])
#print(list1[3])
#print(list1[4])
#negative indexing:
#print(list1[-1])
#print(list1[-2])
#print(list1[-3])
#print(list1[-4])
#print(list1[-5])
#we can also access the list items using negative indexing
#example:-5 -4 -3 -2 -1
#print(list1[-1:3])
#slicing in list:
#slicing is taken out of a part from the main list 
#slicing will extract the part or sublist using [start index:end index]
#example:
#slcl=["apple","banana","cherry","orange","kiwi","melon","mango"]
#print(slcl[2:5])
#print(slcl[:4])
#print(slcl[-3:])
#adding elements in list :
# we can add new values to list in different ways:
#1.append
#2.insert
#3.extend
#example: add bhramandham, after the deepika p
#list1=["deepika","samantha","Bhabhi"]
#removing elements in list 
#remove the item in list in different ways 
#1.remove():removes or deletes the first occurrence of the specified value
#2.pop(): deletes the item from the list at a perticular position 
#3.clear():deletes the all items from the list 
kalkicast=["ram","laxman","bharath","shatrughan"]
kalkicast.remove("bharath") 
print(kalkicast)
kalkicast.pop(2)
print(kalkicast)
kalkicast.clear()
print(kalkicast)
kalkicast.append("bhramandham")
print(kalkicast)    
kalkicast.insert(1,"bhramandham")
print(kalkicast)
kalkicast.extend(["bhramandham","anil"])
print(kalkicast)            
#mathematical operators in lists
#concatination:joins the 2 lists togeather in one list
a=[1,2]
b=[3,4,]
c=a+b
print(c)
#repetation:repeats the elements in the list multiple times 
a=[1,2]
n=int(input("enter the n value:"))
b=a*n
print(b)
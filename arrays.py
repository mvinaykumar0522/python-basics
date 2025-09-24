# #arrays in python :
# l=[10,10.5,"hello",True]
# a=[10,20,30,40,50]
# a=[10.5,20.2,30.3,40.4,50.5]
# #arrays defination:
# # an array is collection of elements of the same datatype stored in continuous memory location 
# #array are used to store multiple values in a single variable .
# #why arrays?
# #easy to manage multiple values.
# #allows faster operations like searching and sorting.
# #useful in mathematica and scientific problems 
# #save memory 
# #array vs lists:
# #importing the array module 
# import array as arr
# #creating an array:
# numbers=arr.array('i',[10,20,30,40,50])#array of integers   
# print(numbers)
# #array of floats:
# float_numbers=arr.array('f',[10.5,20.5,30.5,40.5,50.5])
# print(float_numbers)
# #accessing elements in an array:
# print(numbers[0])#10
# print(numbers[1])#20
# print(numbers[2])#30
# print(numbers[3])#40
# print(numbers[4])#50
# print(numbers[-1])#50
# print(numbers[-2])#40
# print(numbers[-3])#30
# print(numbers[-4])#20
# print(numbers[-5])#10
# #slicing in an array:
# print(numbers[1:4])#[20,30,40]
# print(numbers[:3])#[10,20,30]
# print(numbers[2:])#[30,40,50]
# print(numbers[:])#[10,20,30,40,50]
# #modifying elements in an array:
# numbers[2]=35
# print(numbers)#array('i',[10,20,35,40,50])
# #adding elements in an array:
# numbers.append(60)
# print(numbers)#array('i',[10,20,35,40,50,60])
# numbers.insert(1,15)
# print(numbers)#array('i',[10,15,20,35,40,50,
# #60])
# #removing elements in an array:
# numbers.remove(35)
# print(numbers)#array('i',[10,15,20,40,50,60])
# numbers.pop(2)
# print(numbers)#array('i',[10,15,40,50,60])
# numbers.pop()
# print(numbers)#array('i',[10,15,40,50])
# #iterating through an array:
# for i in numbers:
#     print(i)
# #array methods:
# print(len(numbers))#4
# print(max(numbers))#50
# print(min(numbers))#10
# print(sum(numbers))#115
# print(numbers.index(40))#2
# print(numbers.count(15))#1
# #to convert a list into an array:
# list1=[1,2,3,4,5]
# array1=arr.array('i',list1)
# print(array1)#array('i',[1,2,3,4,5])    
# #to convert an array into a list:
# list2=array1.tolist()
# print(list2)#[1,2,3,4,5]
# print(type(list2))#<class 'list'>
# #multidimensional arrays:
# matrix=arr.array('i',[1,2,3,4,5,6,7,8,9])
# #2D array 3x3 matrix
# row1=matrix[0:3]
# row2=matrix[3:6]
# row3=matrix[6:9]
# print(row1)#array('i',[1,2,3])
# print(row2)#array('i',[4,5,6])
# print(row3)#array('i',[7,8,9])
# #accessing elements in 2D array:
# print(row2[1])#5
# print(row3[2])#9
# #nested arrays:
# nested_array=arr.array('i',[1,2,3,4,5,6
# ,7,8,9])
# nested_array_2d=[nested_array[0:3],nested_array[3:6],nested_array[6:9]] 
# print(nested_array_2d)#[array('i',[1,2,3]),array('i',[4,5,6]),array('i',[7,8,9])]
# print(nested_array_2d[1][2])#6
# #array operations:
# array_a=arr.array('i',[1,2,3])
# array_b=arr.array('i',[4,5,6])
# #concatenation
# array_c=array_a+array_b
# print(array_c)#array('i',[1,2,3,4,5,6])
# #repetition
# array_d=array_a*3
# print(array_d)#array('i',[1,2,3,1,2,3,1,2,3])
# #slicing
# array_e=array_c[2:5]
# print(array_e)#array('i',[3,4,5])
# #looping through an array
# for i in array_a:
#     print(i)
# #nested tuple:
# t=(10,(20,30),(40,50))
# print(t[2][1])
# #nested dictonary
# students={
#     "s1":{"name":"vinay","roll no":"g2"},
#     "s2":{"name":"harshit","roll no":"g5"},
#     "s3":{"name":"rohit","roll no":"j8"}
# }
# print(students["s2"]["name"])#harshit
# print(students["s3"]["roll no"])#j8 
# print(students["s1"]["name"])#vinay
# print(students["s1"]["roll no"])#g2
# #modifying nested dictionary values:
# students["s2"]["name"]="rahul"
# print(students["s2"]["name"])#rahul
# students["s3"]["roll no"]="k9"
# print(students["s3"]["roll no"])#k9
# #adding new key-value pair in nested dictionary:
# students["s4"]={"name":"anil","roll no":"m1"}
# print(students["s4"]["name"])#anil
# print(students["s4"]["roll no"])#m1
# #removing key-value pair from nested dictionary:
# del students["s1"]
# print(students)
# #loops for dictonary
# # l=[10,20,30,40,50]
# # for i in range(0,5):
# #     print(l[i])
# # biodata={
# #     "name":"sai ram ",
# #     "roll .no":"g2",  
# #     "branch":"cse ai/ml",
# #     "place":"hyderabad"
# # }
# # #loops
# for i in biodata.keys():
#     print(i)
# # for i in biodata.values():
# #     print(i)
# # # for i in biodata.items():
# #     print(i)
# #nested tuple:
# t=(10,(20,30),(40,50))
# print(t[2][1])
# #nested dictonary
# students={
#     "s1":{"name":"vinay","roll no":"g2"},
#     "s2":{"name":"harshit","roll no":"g5"},
#     "s3":{"name":"rohit","roll no":"j8"}
# }       
# print(students["s2"]["name"])#harshit
# print(students["s3"]["roll no"])#j8
# print(students["s1"]["name"])#vinay
# print(students["s1"]["roll no"])#g2
# #modifying nested dictionary values:
# students["s2"]["name"]="rahul"
# print(students["s2"]["name"])#rahul 
# students["s3"]["roll no"]="k9"
# print(students["s3"]["roll no"])#k9
# #adding new key-value pair in nested dictionary:
# students["s4"]={"name":"anil","roll no":"m1"}
# print(students["s4"]["name"])#anil
# print(students["s4"]["roll no"])#m1
# #removing key-value pair from nested dictionary:
# del students["s1"]
# print(students)
# #loops for dictonary
# l=[10,20,30,40,50]
# for i in range(0,5):
#      print(l[i])
# biodata={
#     "name":"sai ram ",
#      "roll .no":"g2",
#      "branch":"cse ai/ml",
#      "place":"hyderabad"
# }
# # accessing values in dictonary
# print(biodata["name"])#sai ram
# print(biodata["roll .no"])#g2
# print(biodata["branch"])#cse ai/ml
# print(biodata["place"])#hyderabad
# #modifying values in dictonary
# biodata["place"]="bangalore"
# print(biodata["place"])#bangalore
# biodata["branch"]="cse ds"
# print(biodata["branch"])#cse ds
# #adding new key-value pair in dictonary
# biodata["college"]="xyz college"
# print(biodata["college"])#xyz college
# biodata["year"]="3rd year"
# print(biodata["year"])#3rd year
# #removing key-value pair from dictonary
# del biodata["roll .no"]
# print(biodata)
# del biodata["year"]
# print(biodata)
#extended example:
# biodata={
#     "name":"sai ram ",
#     "roll .no":"g2",
#     "branch":"cse ai/ml",
#     "place":"hyderabad",
#     "skills":["python","java","c++","html","css","javascript"],
#     "education":{"10th":"95%","12th":"90%","graduation":"8.5 cgpa"},
#     "projects":[{"name":"project1","description":"description1"},{"name":"project2","description":"description2"}]
# }
# #accessing values in dictonary
# print(biodata["name"])#sai ram
# print(biodata["skills"][0])#python
# print(biodata["education"]["graduation"])#8.5 cgpa
# print(biodata["projects"][1]["name"])#project2
# #modifying values in dictonary
# biodata["place"]="bangalore"
# print(biodata["place"])#bangalore
# biodata["education"]["12th"]="92%"
# from ast import arg
# numbers=arg.array('i',[10,15,40,50])
# print(numbers)#array('i',[10,15,40,50])
# #extend():
# numbers.extend([70,80,90])
# print(numbers)#array('i',[10,15,40,50,70,80,90])
# #reverse():     
# numbers.reverse()
# print(numbers)#array('i',[90,80,70,50,40,15,
# #append():
# numbers.append(100)
# print(numbers)#array('i',[90,80,70,50,40,15,100])
# #buffer_info(): 
# print(numbers.buffer_info())#(140703303123712,7)
# #typecode:
# print(numbers.typecode)#i
# #insert():
# numbers.insert(2,75)
# print(numbers)#array('i',[90,80,75,70,50,40,15,100])
# #tolist():
# list2=numbers.tolist()
# print(list2)#[90,80,75,70,50,40,15,100]
# print(type(list2))#<class 'list'>
# #deleting an array:
# del numbers 
# print(numbers)#NameError: name 'numbers' is not defined
# #output: NameError: name 'numbers' is not defined
#numpy 
#numpy(numerical python) is a python liberary used for scientific and mathematical computing 
# it proides:
#--> powerfull array object(more effective than python lists.)
#--> vectorised operations(fast element-wiser calculation)
#--> support for linear algebra , statistics, random number operation etc...  
# import numpy as np
# a1d=np.array([1,2,3,4,5])
# print(a1d)
# a2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a2d)
# a=np.array([1,2,3,4,5])
# print(a.ndim)
# print(a2d.ndim)
# print(a.shape)
# print(a2d.size)
# print(a2d.dtype)
# import numpy as np
# print(np.zeros(6))
# print(np.ones(12))
# print(np.arange(1,11,1))
# print(np.arange(0,11,2))
# print(np.arange(1,11,2))
# print(np.linspace(0,1,3))
# a=np.array([1,2,3,4,5])
# l=[1,2,3,4,5]
# print(a+6)
# print(a-1)
# print(a*2)
# print(a/2)
# print(a//2)
# print(a**6)
# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.median(a))
# print(np.std(a))
# print(np.cumprod(a))
# mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
# print(mat1+mat2)
# print(mat1**2)

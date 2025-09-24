#function 
#a function is a block of code that performs a specific task.
#it allows us to group instructions togeather and reuse them whenevr we need 
#instead of writing the same code again and again,we just define a function once and call it whenever required.
#syntax:
# def function_name(parameters):
#     #function body code 
#     return value #optional 
# function_name()
# # example =
# def greet():
#     print("hello world!!")

#calling a function:
#calling a function means teling python to run the code inside a function by using its name followed by paranthese().
#if the function needs input(parameter),we provide values (arguments)inside the parantheses.
#when we call a function,python jumps to the function,excutes its code ,and then comes back to continue th e program 
# def greet():
#         print("hello world!!")
# greet()

#passing parameters & arguments 
#parameters: a variable decleared inside the function definition it acts like an empty container waiting tp recive a value 
#arguments:the actual value we pass into the function when calling it . it fills the empty container(parameters)
#example:
# def greet(name):
#         print("hello",name)
# greet("vinay")
#same task without function
# name="vinay"#here name is input variable(parameter), and "vinay"i sthe value of parameter(argument).
# print("hello",name)

#types og function arguments:
#A--positional argument:
#when we pass arguments in same order as the function parameter,they are called as positional arguments.
#here the order (position) is very important.
# def greet(name,rollno):
#         print("hello",name,"your rollno is",rollno)
# greet("nandhan","l6")#step1:function calling 

#b.keyword arguments:
#when we pass value or arguments by writing the parameters(variables=values),they are called as keyword arguments.
# def greet(rollno,name):
#         print("hello",name,"your rollno is",rollno)
# greet(name="vinay",rollno="g2")

#default argument:
#when a parameter has a default value (assigning the value in parameter) in the function definition,it becomes a default argument.
# def greet(name="rajesh"):
#         print("namstey",name)
# greet()
# greet(name="vinay")

#d. variable arguments:
#l=10,20,30,40,50
# def sum1(*list1):
#         sum2=0
#         for i in range(len(list1)):
#                 sum2=sum2+list1[i]
#         print(sum2)#150 
#         print(type(list1))

# sum1(10,20,30,40,50)
#2.**kwargs:(keyword variable-length arguments)
#collects multiple key=value pair into a dictionay 
# def details(**info):
#         for i,j in info.items():
#                 print(i,":",j)
# details(name="vinay",rollno="g2",branch="cse ai/ml")
# #scope of the variable:
# x=10#global variable 
# def var1():
#         x=5#local variable 
#         print("inside var1 function",x)
# var1()
# def var2():
#         print("inside var2 function",x)
        

#it is usually used for short,simple operation.
#syntax
#lambda function:expression 
# #normal function 
# def sqe(a):
#         print(a*a)
# sqe(5)
# #lambda function 
# squ=lambda a:a*a
# print(squ(5))
#the whole character whchic is given in double codes or single codes is called as string 
#real numbers imaginary 
# bollean: true or false 
#factorial 
#5!=5*4*3*2*1
def factorial(n):
    for i in range(n,0,-1):
        fact=fact*1
        print(fact)
        factorial(5)
        factorial(4)

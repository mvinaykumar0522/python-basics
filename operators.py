#searching and cheking :
#in operator:
#a= [2,4,6,8,8,10,12,14]
#if 2 in a:
#   print("yes!! item is present in the list")
#not in operator:
#print(3 not in a )
# index methon or index():
#print(a.index(8))
#count ()
#print(a.count(8))
#for i in range(10):
#   if i==8:
    #   cnt = int+1
#print(cnt)
#sorting [2,5,1,8]
#it arrange elements either in asccending order(small to large) descending order(large to small )
#reversing:reversing()
#it flips the list so the last element will becomes the first element.
#st=[25,12,5,31,13,18,7,45,8,55,68]
#st.sort()
#print(st)
#st.reverse()
#print(st)
#st1=[25,8,4,7,10]
#st1.sort(reverse=True)
#copying the list:
# #coping creates the new list with the sane elements, so changes in the new list will not affect the original list
# frnd1=["ram","ravi","raju","anil","sunil","latha","delip loude","satish mut marey","rajendar londe"]
# frnd2=frnd1.copy()
# print(frnd2)
# frnd2.append("rahul")
# print(frnd2)    
# #built in function
# #python programming provides many ready-made functions to work with the items 
# st=[25,12,5,31,13,18,7,45,8,55,68]
# #len():ruturns the number of elements 
# print(len(st))
# #max():returns the maximum element from the list 
# print(max(st))
# #min():returns the maximum element from the list 
# print(min(st))
# #sum():returns the total sum of all numeric elements 
# print(sum(st))
# #pirticular
# #mutipli values usung input data to;the list 
# a=input("enter the multiple values:").split()# 10 20 30 40 50 
# print(a)
# a.sort()
# a=list(map(int,input("enter the multiple values:").split()))# 10 20 30 40 50 
# print(a)
# a.sort()
#traversing a list:
#accessing the elements using a loop 
#using for loop 
# cars=["thar","bmw","mercedes","konigssege"]
# print(len(cars))
# for car in range(0,1):
#     print("cars=",car)
# #using index with for loop 
# a=len(cars)
# for i in range(0,a):
#           print("cars",i,"=",cars[i])
#adding elements using for loop 
# list1=[]
# for list in range(0,5):
#     a=input("value:")
#     list1.append(a)
# print(list1)
#give the input value to the lists from 1 to 10 
# list1=[]
# n=int(input("enter the number of list values:"))#10 
# for i in range(n):
#     list1.append(i)
# print(list1)
#sum of lists items=10 20 30 40 50 without using sum function
# list1 = [10, 20, 30, 40, 50]  # Example list initialization
# sum=0
# for i in list1:
#     sum=sum+i
# print("sum of list items:",sum)
#convert ["p","y","t","h","o","n"] to "python"
# list2=["p","y","t","h","o","n"]
# str1=""
# for i in list2:
#     str1=str1+i
# print(str1)
# #list comprehension:
# #it is a concise way to create lists    
# #syntax:
# #[expression for item in iterable if condition==True]
# #squares of numbers from 1 to 10
# squares=[i*i for i in range(1,11)]      
# print(squares)
# #even numbers from 1 to 20
# even=[i for i in range(1,21) if i%2==0]
# print(even)
# #odd numbers from 1 to 20
# odd=[i for i in range(1,21) if i%2!=0]  
# print(odd)
# #cubes of numbers from 1 to 10
# cubes=[i**3 for i in range(1,11)]
# print(cubes)
# #numbers divisible by 3 from 1 to 30
# div_by_3=[i for i in range(1,31) if i%3
# ==0]
# print(div_by_3)
# #uppercase letters from a list of lowercase letters 
# lowercase=['a','b','c','d','e']
# uppercase=[i.upper() for i in lowercase]
# print(uppercase)
# #vowels from a list of letters
# letters=['a','b','c','e','i','o','u','x','y']
# vowels=[i for i in letters if i in 'aeiou']
# print(vowels)
# #lengths of words from a list of words
# words=['apple','banana','cherry','date']
# lengths=[len(i) for i in words]
# print(lengths)
# #positive numbers from a list of numbers
# numbers=[-10,15,-20,25,-30,35]
# positive_numbers=[i for i in numbers if i>0]
# print(positive_numbers)
# #flatten a list of lists
# list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
# flattened=[i for sublist in list_of_lists for i in sublist] 
# print(flattened)
# #convert a list of strings to a list of integers
# str_numbers=['10','20','30','40']
# int_numbers=[int(i) for i in str_numbers]
# print(int_numbers)
# #filter out negative numbers from a list
# mixed_numbers=[-10,15,-20,25,-30,35]
# non_negative=[i for i in mixed_numbers if i>=0]
# print(non_negative)
# #convert a list of temperatures from Celsius to Fahrenheit
# celsius=[0,10,20,30,40]
# fahrenheit=[(i*9/5)+32 for i in celsius]
# print(fahrenheit)
# #find common elements between two lists
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# common_elements=[i for i in list1 if i in list2]
# print(common_elements)
# #remove duplicates from a list
# list_with_duplicates=[1,2,2,3,4,4,5]
# list_without_duplicates=list(set(list_with_duplicates))
# print(list_without_duplicates)
# #generate a list of tuples containing numbers and their squares
# numbers=[1,2,3,4,5]
# squared_tuples=[(i,i*i) for i in numbers]
# print(squared_tuples)
# #generate a list of even squares from 1 to 20
# even_squares=[i*i for i in range(1,21) if i%2==0]
# print(even_squares)
# #generate a list of words that start with a specific letter
# words=['apple','banana','cherry','date','avocado']
# a_words=[i for i in words if i.startswith('a')]
# print(a_words)
# #generate a list of numbers that are multiples of both 2 and 3
# multiples_of_2_and_3=[i for i in range(1,101)
#     if i%2==0 and i%3==0]
# print(multiples_of_2_and_3)
# #generate a list of strings with length greater than 3
# strings=['hi','hello','hey','greetings','yo']
# long_strings=[i for i in strings if len(i)>3]
# print(long_strings)
# #generate a list of squares of odd numbers from 1 to 20
# odd_squares=[i*i for i in range(1,21) if i%2!=0]
# print(odd_squares)
# #generate a list of numbers that are not divisible by 5
# not_divisible_by_5=[i for i in range(1,51) if i%5!=0]
# print(not_divisible_by_5)
# #generate a list of lowercase letters from a list of mixed case letters
# mixed_case=['A','b','C','d','E']
# lowercase_letters=[i.lower() for i in mixed_case]
# print(lowercase_letters)
# #generate a list of words with vowels removed
# words_with_vowels=['apple','banana','cherry','date']
# words_without_vowels=[''.join([char for char in word if char not in 'aeiou']) for word in words_with_vowels]
# print(words_without_vowels)
# #generate a list of numbers raised to the power of their index
# numbers=[10,20,30,40,50]
# powered_by_index=[num**idx for idx,num in enumerate(numbers)]
# print(powered_by_index)
# #generate a list of strings reversed
# strings=['hello','world','python','rocks']
# reversed_strings=[s[::-1] for s in strings]
# print(reversed_strings)
# #generate a list of tuples containing numbers and their cubes
# numbers=[1,2,3,4,5]
# cubed_tuples=[(i,i**3) for i in numbers]
# print(cubed_tuples)
# #generate a list of prime numbers from 1 to 100
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# prime_numbers=[i for i in range(1,101) if is_prime(i)]
# print(prime_numbers)
# #generate a list of strings converted to title case
# strings=['hello world','python programming','list comprehension']
# title_case=[s.title() for s in strings]
# print(title_case)
# #generate a list of numbers that are perfect squares
# perfect_squares=[i*i for i in range(1,11)]
# print(perfect_squares)
# #generate a list of numbers that are perfect cubes
# perfect_cubes=[i**3 for i in range(1,11)]
# print(perfect_cubes)
#find the maximum and minimum number from list without using max() and min()
# numbers=[45,23,67,89,12,5,90,34]
# max_num=numbers[0]
# min_num=numbers[0]
# for num in numbers:
#     if num>max_num:
#         max_num=num
#     if num<min_num:
#         min_num=num
# print("maximum number is:",max_num)
# print("minimum number is:",min_num)
# numbers.sort()
# print(numbers)
#searching for an element in a list
# numbers=[45,23,67,89,12,5,90,34]  
# target=int(input("enter the number to search:"))#67
# found=False
# for num in numbers:
#        if num==target:
#             found=True
#             break
# if found:
#     print(target,"is found in the list")
# else:
#    print(target,"is not found in the list")
#count even and odd numbers 
# numbers=[46,23,67,89,12,5,90,34]  
# even_count=0
# odd_count=0
# for num in numbers:
#     if num%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("even numbers count:",even_count)
# print("odd numbers count:",odd_count)
# #reverse a list without using reverse()
# numbers=[45,23,67,89,12,5,90,34]
# reversed_list=[]
# for i in range(len(numbers) -1,-1,-1):
#     reversed_list.append(numbers[i])
# print("reversed list:",reversed_list)
# # numbers.sort()
# # print(numbers)
# #remove all negative number using loop 
# numbers=[45,-23,67,-89,12,-5,90,34,-1]
# positive_numbers=[]
# for num in numbers:
#     if num>=0:
#         positive_numbers.append(num)
# print("list with positive numbers:",positive_numbers)
#multiply each element in the list
# numbers=[1,2,3,4,5]
# multiplied_list=[]  
# factor=int(input("enter the factor to multiply:"))#3
# for num in numbers:
#     multiplied_list.append(num*factor)
# print("multiplied list:",multiplied_list)
#write a program to find the average of all numbers in a list
numbers=[10,20,30,40,50]
total=0
for num in numbers:
    total+=num
average=total/len(numbers)
print("average of the list is:",average)
# #count how many positive and negative numbers and zero values are there in the list
# numbers=[45,-23,0,67,-89,12,-5,90,34,-1,0]
# positive_count=0
# negative_count=0
# zero_count=0
# for num in numbers:
#     if num>0:
#         positive_count+=1
#     elif num<0:
#         negative_count+=1
#     else:
#         zero_count+=1
# print("positive numbers count:",positive_count)
# print("negative numbers count:",negative_count)
# print("zero values count:",zero_count)
# #remove duplicate elements in the list 
# numbers=[1,2,2,3,4,4,5,5,5]
# unique_numbers=[]
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print("list with unique elements:",unique_numbers)
# #write a program to seperate even and odd numbers into two lists 
# numbers=[45,23,67,89,12,5,90,34]
# even_numbers=[]
# odd_numbers=[]
# for num in numbers:
#     if num%2==0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
# print("even numbers list:",even_numbers)
# print("odd numbers list:",odd_numbers)
#take a list of names and print the longest name
# names=["ram","ravi","raju","anil","sunil","latha","delip","satish","rajendar"]
# longest_name=names[0]       
# for name in names:
#     if len(name)>len(longest_name):
#         longest_name=name
# print("longest name is:",longest_name)
# dictonary:
# dictonary is a inbuilt data type ,which is used to store multiple values in a single variable 
# dictonary stores the data in the form of key-values paris.
# a={s1:"name":"chota bheem"}
# each key is a unique and works as an index to access its corresponding values 
# keys are immutable(cannot be changed) but values are mutable (can be changed )
# dictonaries are ordered,mutable,do not allows the duplicate keys 
# loops for dictonary 
# l=[10,20,30,40,50]
# for i in range(0,5):
#     print(l[i])
# biodata={
#     "name":"sai ram ",
#     "roll .no":"g2",
#     "branch":"cse ai/ml",
#     "place":"hyderabad"
# }
# #loops 
# for i in biodata.keys():
#     print(i)
# #
# for i in biodata.values():
#     print(i)
# #
# for i in biodata.items():
#     print(i)
#nested tuple:
t=(10,(20,30),(40,50))
print(t[2][1])
#nested dictonary 
students={
    "s1":{"name":"vinay","roll no":"g2"},
    "s2":{"name":"harshit","roll no":"g5"},
    "s3":{"name":"rohit","roll no":"j8"}
}
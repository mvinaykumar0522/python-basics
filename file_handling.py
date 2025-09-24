# file=open("student.txt","w")
# print("file created")
# file.close()
#types of read():
#1.read()=>
# file=open("student.txt","r")
# content=file.read()
# print(content)
# file.close
#2.readline()=>
# file=open("student.txt","r")
# content=file.readline()
# content1=file.readline()
# content2=file.readline()
# print(content)
# print(content1)
# print(content2)
# file.close
#3.readline()=>
# file=open("student.txt","r")
# content=file.read()
# print(content)
# file.close
file=open("student1.txt","w")
#write,writelines
file.write("hello c++\n")
file.write("hello python\n")
lines=["hello vinay\n","hello rajesh\n","hello world\n","hello python\n"]
file.writelines(lines)
file.close

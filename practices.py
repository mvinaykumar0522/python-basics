#area of triangle 
height=int(input("Enter the height of triangle: "))
base=int(input("Enter the base of triangle: "))
aot=1/2*base*height
print("Area of triangle is: ",aot)
#finding square and cube of a number 
a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
square=a**2
cube=b**3
print("square of ",a,"is:",square)
print("cube of ",b,"is:",cube)
speed=int(input("Enter the speed of car in km/hr: "))
if speed>60:
    print("You are driving too fast")
    print("You will be fined")
else:
    print("You are driving safe")
print("End of the program")
if 50>30:
    print("50 is greater than 30")
    if 50>20:
        print("50 is also greater than 20")
    if 50>40:
        print("50 is also greater than 40")
print("End of the program")

#km->m/m->cm
km=int(input("Enter the distance in km: "))
m=km*1000
cm=m*100
miles=distance*1.6 # type: ignore
print("Distance in meter is: ",m)
print("Distance in centimeter is: ",cm)
print("Distance in miles is: ",miles)
#find the number is even or odd\
num=int(input("Enter a number: "))
if num%2==0:
    print(num,"is an even number") 
else:
    print(num,"is an odd number")
print("End of the program")
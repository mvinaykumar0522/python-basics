i=5
if 1%2==0:
    print("odd")
else:
    print('even') 

#1 zerodivisionerror
#it is an exectpion which divides a number by zero
try:
    a=int(input("enter the numerator:"))
    b=int(input("enter the dinominator:"))
    c=a//b
    print(c)
except ZeroDivisionError:
    print("error:division by zero is not possible")
    #name error 
try:
    sum="5"+5
    print(sum)
except TypeError:
    print("invalid type operation.")
#name error 
try:
    print(mult)
except NameError:
    print('variable not decleared' )
    

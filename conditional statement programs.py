#control flow statement 1. Conditional statement 2. Transfer statement 3. Loop Statement
#conditional Statements 1. single 2. biconditional 3. nested 4. ladder
'''single condition: returns true if cond is matched. syntax
if exp/cond:
    statement/code'''

#wap to sum of digits of three digit no with cond. statement
a= int(input("enter 3 digit no:"))
if a >=100 and a <=999:
    b=a//100
    c=a%100
    d=c//10
    e=c%10
    print("sum of 3 digits are",b+d+e)

#example of exp
if 5:
    print("true")
if 0:
    print("false")
if -6:
    print("true")

#wap to find given year is leap or not leap = 366 normal = 365
year = int (input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("normal year")

#wap to find a number is even or odd
a = int(input("Enter any number:"))
if a%2==0:
    print("number is even")
else:
    print("Number is odd")

#wap which is divisible by 3 and 5
n = int (input("Enter any number:"))
if n%3==0 and n%5==0:
    print("number is divisible by 3&5 ")
else:
    print("not divisible")

# wap to find largest given two no.s
a =int(input("enter first no:"))
b = int(input("enter second no:"))
if a>b:
    print ("first no is largest")
elif a<b:
    print("second no is largest")
else:
    print("no is equal or invalid")


#wap to given char is vowel or not
s = input("enter any character:")
if (s=="a,e,i,o,u") and (s=="A,E,I,O,U"):
    print("char is vowel")
else:
    print("char is consonant")


#nested condition
'''
if cond/exp :
    statement/code
    if cond / exp:
        statemnet/code
    "
    "
    "
    "
    else:
        statement/code
else:
    statement/code
'''
#wap to match correct pass and account no
a = int(input("Enter your account no:"))
if a == 5460:
    print("correct")
    p = int(input("Enter password:"))
    if p == 1010:
        print("correct")
    else:
        print("wrong")
else:
    print("wrong")


#wap to apply for post enter % of 10th if 80+ then ask 12th if 70+ msg you are eligible
t = float(input("Enter your 10th percentage:"))
if t >= 80:
    a = float(input("Enter your 12th percentage:"))
    if a >= 70:
        print("you are eligible for clerk post")
    else:
        print("you are eligible for peon")
else:
    print("not eligible for any post")




#wap due you have adhar card   if yes dur u have pan card if yes passsport if yes eligible for visa
a = input("due you have adhar card")
if a == "yes" or a=="YES" or a=="Yes":
    p = input("due you have pan card")
    if p == "yes" or p=="YES" or p=="Yes":
        pa = input("due you have passport")
        if pa == "yes" or pa=="YES" or pa=="Yes":
            print("you are eligible for visa")
        else:
            print("not eligible")
    else:
            print("not eligible")
else:
            print("not eligible")

#wap for swaping
a = int(input("enter first no:"))
b = int(input("enter second no:"))
a,b=b,a
print("after swaping",a,b)

#swaping with 3rd variable
p = int(input("enter first no:"))
q = int(input("enter second no:"))
r=p
p=q
q=r
print("after swaping",p,q)

#swaping without 3rd variable real method
c = int(input("enter first no:"))
d = int(input("enter second no:"))
c=c+d #3+2=5,c=5
d=c-d #5-2 , d=3
c=c-d #5-3, c=2
print("after swaping",c,d)

#wap to add digits of a three digit and printing their reverse no 100 to 999
a = int(input("Enter three digit No:")) #555
b=a//100 #555//100 = 55
c=a%100 #rem=55
d=c//10 #55//10=5
e=c%10 #rem=5
print("sum of digits:",b+d+e) #output=15
print("reverse of no:",b*1+d*10+e*100) #reverse the three digits
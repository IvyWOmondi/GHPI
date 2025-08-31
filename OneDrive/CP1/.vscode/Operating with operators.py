#Section 1
a=50
a+=1 #add and assign
print("Variable a incremented:", a)
a-=1
print("Variable a decremented:", a)
a*=5
print("Variable a multiplied:", a)
a/=2
print("Variable a divided", a)

#Section 2
b=5
c=True
d=False

#Section 3 Testing 'a' and 'b'
if a>50 and b<10:
 print("a is greater than 50 and b is less than 10")
else:
 print("Something went wrong")

if a<500 and a>3:
 print("a is less than 500 and greater than 3")
else:
 print("Something went wrong") # a= 125 which is less than 500 and greater than 3

#Section 4 Testing 'c'
if c:
 print("c is true")
else:
 print("c is false")

#Section 5 Testing 'd'
#Logical NOT
if d is not True:
 print("d is false")
else:
 print("d is true") #Output:d is false 

 #String
name="Ivy Wanjiku Omondi"
print(name)
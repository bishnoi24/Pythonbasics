# string formation 

name = " Mona Bishnoi"
age = "31"
print(f"My name is {name} and age is {age}")

# string Indexing 

name = "master"
print(name[0])

# string Slicing  

print(name[0:3])

# input function (Add only sting not int value )

#name = input("Enter your name : ")
#age = input ("Enter your age: ")
#print(f"name: {name} and age:{age}")

# Int fundtion 

#num1 = int(input("Enter your num1 : "))
#num2 = int(input ("Enter your num2: "))
#num3 = num1 + num2
#print(num3)


#len function

Name = "Master"

#print(len(Name))

#lower & upper function 

print(Name.lower())
print(Name.upper())

# count fuction (Find count a variable and valune into the list[] and tuple())

#title function 

print(Name.title())

# Find and replace fuction 

#string.replace("old","new")

print(Name.replace("Master","First"))

strfind  =  Name.find ("Master")
#Find index and print string according it 

print(strfind)
print(Name[5])


#Rang and step function

#rang (start,stop, step)

rangef = range(0,10)
stepf = range(0,10,2)
for i in rangef:
    print (i)
for i in stepf:
    print(i)

#center function 

# string.center(widht,[fillchar])

var = Name.center(10,"*")
print(var)


# in keyword 

if "master" in Name:
    print("hello")





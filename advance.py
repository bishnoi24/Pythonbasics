# list in python (array )
# IN for loop

data = ["Mona","Bishnoi",30]
for i in data:
    print (i)

#indexing 
data1 = ["Mona","Bishnoi",30]
print(data1[1])

#slicing

data2 = ["Mona","Bishnoi",30]

print(data2[0:2])

#append
data3 = ["Mona","Bishnoi",30]
data3.append("software eng")
print(data3)

# Change data using indexing 

data4 = ["Mona","Bishnoi",30]
data4[2]  = 31
print(data4)

#del (delete by index )
data5 = ["Mona","Bishnoi",30]
del data5[2]
print(data5)

#remove (remove given value )
data5.remove("Mona")
print(data5)

#pop (remove last element from the list or array )

data5.pop()
print(data5)

# add list 
newlist = ["addnew"]

add = data5 + newlist

print(add)

#copy\
newlistval  = newlist.copy()

print(newlistval)

# extend
newlist1 = ["test","test1"]
newlist.extend(newlist1)
print(newlist)

# clear
print(newlist1.clear())
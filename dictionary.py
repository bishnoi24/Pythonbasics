# it is a datastructure which is unordered collection of item in key valu pair in it we
#store data in dictionary like string and flot,int etc

# data = {}
# print(type(data))

# create dict 

# data1 =[]
# name = dict(data1)
# print(name)

# use of dict

data = {"Name":"Mona",
        "age":30,
        "role":"eng"}

print(data)

# for loop with val 

for i in data.values():
    print(i)

    
for i in data.items():
    print(i)

# indexing 

data1 = {"Name":"Bishnoi",
        "age":30,
        "role":"eng"}
data1['Name'] = "Mona"
print(data1['Name'])

# add data using indexing 

# in 

# update function 
data21 = {"last Name":"bishnoi",
        "agew":30,
        "rolew":"eng"}
data22 = {"Name":"Mona",
        "age":350,
        "role":"eng"}

data3 =  data21.update(data22)
print(data3)

#Delete  Function 

data221 = {"last Name":"bishnoi",
        "agew":30,
        "rolew":"eng"}
del data221['agew']
print(data221)

#pop fuction 

data221.pop('rolew')
print(data221)

# Get function 
data11 = {"Name":"Bishnoi",
        "age":30,
        "role":"eng"}

print(data11.get('age'))


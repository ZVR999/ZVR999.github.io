##Print Stuff
print("Hello world")


#Create a tuple
x = (5, 6, 'cupcakes', 'frosting')

print(x[2])
print(len(x))

#Create a list
y = [5, 6, 'cupcakes', 'frosting']

print(y[3])
print(len(y))

y.append("Last Value")
y.insert(0,"First Value")
y.insert(3,"Forth Value")

print(y)

#Remove value in 3rd index position
y.pop(2)
print(y)

#Remove the first occurance of "cupcakes"
y.remove("cupcakes")
print(y)

#Reverse the order of list y
y.reverse()
print(y)

#Create list z
z = [1,34,45,67,34,75,1,34,100]
#Sort list z in reverse/decending order
z.sort(reverse=True)
print(z)

dicti = {'key1': 1, 'key2': "John", 'key3':"Mia"}

print(dicti['key3'])

print(dicti.keys())
print(dicti.values())
print(dicti.items())

for item in dicti.items():
    print(item)

for key in dicti.keys():
    print(key)

for value in dicti.values():
    print(value)
    if value == "John":
        print("This is one piece of.." + value)
    if value == 1:
        dicti.pop('key1')
        del dicti['key3']
        break
print(dicti)

tet1 = {1,4,5,3,123,189}

tet2 = {1,34,45,67,34,75,1,34,100}

print(tet1)
z = tet1.difference(tet2)
tet1.add("Add ME")
print(tet1)
tet1.update(y)
print(tet1)
print(tet1.intersection(tet1,y))
print(z)



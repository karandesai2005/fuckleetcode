#hasmaps
mymap = {}

mymap["alice"] = 23
mymap["dog"] = 12
print(mymap)
print(len(mymap))
#we can update
mymap["alice"] = 12
#check if key is there in hashmap
print("dog" in mymap)
mymap.pop("dog")
print(mymap)
print("dog" in mymap)

#dict comprehension

mymap = {i:2*i for i in range(3)}
print(mymap)

#looping through mymap
for key in mymap:
    print(key , mymap[key])

#directly iterate through the list of values !!

for val in mymap.values():
    print(val)

for key, value in mymap.items():
    print(key, value)

#tupples are immutable
tup = (1,2,3)

print(tup)
print(type(tup))
print(tup[0])
#tup[1] = 12 wont work
print(tup[-1]) #print last value

#tuples can be used as keys in hashmap cause list couldnt 
mymap = {(1,2) : 3, 4: 5, (6,7) : "bhodda"}
print(mymap)
print(mymap[(1,2)])


for key, value in mymap.items():
    print(f" {key}:{value}are")

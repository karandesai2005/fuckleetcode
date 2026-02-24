#hashsets is a datastructure that :
'''
-> stores unique values
-> uses hashing to store data so fast opetations
'''
s = {1,2,3,4,2,3,4,5,}
print(s)
print(type(s))
print(len(s))
# we could also assign using this
myset = set()
myset.add(1)
myset.add(2)
print(myset)
for i in range(0,6):
    myset.add(i)

print(myset)
print(1 in myset)
print(7 in myset)

niggaset = { i for i in range(0,11)}
print(niggaset)



#we gonna practice lambda functions
#lamda functions are one line small functions with no name
'''for example'''

#normal addition functions
def add(a,b):
    return a+b

print(add(2,3))
#lamfa version of this function will be
add = lambda a,b: a+b
print(add(3,3))

#square number 

def sqaure(x):
    return x*x

#using lamda

square = lambda x: x*x

print(square(12))

#even or odd function

evenorodd = lambda x: "EVEN" if x%2 == 0 else "ODD"
print(evenorodd(13))



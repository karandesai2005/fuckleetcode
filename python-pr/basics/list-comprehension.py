#list comprehension
arr = [i for i in range(5)]
print(arr)
print(" == 2D ARRAYS ===")
#2d arrays here
arr = [[1] * 4 for i in range(6)]
print(arr)
print(id(arr[0]))
print(id(arr[1]))
'''we created a array of len 4 by saying [1] * 4 and then did that 6 times using for loop '''
arr[0][0] = 12
print(arr)
#this wont work

arr = [[1]*4] * 4
print(arr)
print(id(arr[0]))
print(id(arr[1]))
arr[0][0] = 12
print(arr)


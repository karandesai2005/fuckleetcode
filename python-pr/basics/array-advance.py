#lambda 
arr = ["alice","bob","sundar","karan","het"]

arr.sort()
print(arr)
#now if i wanna sort acc to len of the string then we could do custom sort using lambda
arr.sort(lambda key= x:len(x))
print(arrrr)


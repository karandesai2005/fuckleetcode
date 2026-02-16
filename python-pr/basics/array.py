arr = [1,2,3]
print(arr)
arr.append(4)
arr.append(5)
print(arr)
arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0] = 12
print(arr)
#initialize an array of value of 5
n = 5
#arr = [1]*n
print(arr)

print(len(arr))
#in python -1 is not out of bound its actually last value
print(arr[-2])

#sublisting in python 
arr = [12,23,34,45,56]
print(arr[1:3])


#unpacking in arrays

a,b,c = [1,2,3]
print(a)
print(b)
print(c)
print("looping though arrays simple using range")
#looping in arrays
nums = [1,2,3,4,5,6,7]

for i in range(len(nums)):
    print(nums[i])

print("looping through arrays without index")

for i in nums:
    print(i)

print("looping through arrays with index and value using enumerate function")

for i , n in enumerate(nums):
    print(i,n)
print("looping thoug multiple arrays simultaneously with unpacking")

nums1 = [1,3,5]
nums2 = [2,4,6]

for n1 , n2 in zip(nums1,nums2):
    print(n1,n2)

print("reversing array")
nums2.reverse()
print(nums2)

print("sorting in array")
arr = [1,2,3,4,5]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)


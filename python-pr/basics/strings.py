#strings very similliar like arrays
#they are immutable
#we can update string but it creates a new string
s = "karan"
print(s[::-1]) 
s+="def"
print(s)
print("=====conversion======")
print(int("123") + int("123"))
print(str(123) + str(123))
print("===if i need ASCII val of something use ord====")
print(ord('A'))
print(ord('a'))
print("=====combine a list of string=====")
strings = ["ab","cd","de"]
print("--".join(strings))


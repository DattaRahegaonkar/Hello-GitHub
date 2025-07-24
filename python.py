
str1 = "madam"

length=int(len(str1))

duplicate=""

for i in range(0, length):
    j=i+1
    duplicate+=str1[-j]

if str1 == duplicate:
    print("palindrome")


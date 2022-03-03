a = int(input("Enter a Number: "))
b = a
reversenum = 0
while a > 0:
    reminder = a % 10
    reversenum = (reversenum * 10) + reminder
    a = a // 10
if b == reversenum:
    print(b ," is Palindrome")
else:
    print(b ," is not Palindrome")

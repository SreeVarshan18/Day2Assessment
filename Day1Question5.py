str = input("Enter a String/Sentence: ")
a = str.split()
smallest = largest = a[0]
for i in range(0,len(a)):
    if len(largest)<len(a[i]):
            largest=a[i]
    if len(smallest)>len(a[i]):
            smallest=a[i]
print("'" ,largest,"'" ," is the largest word")
print("'" ,smallest, "'" ," is the smallest word")
#Q5.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a="apple"
b="banana"
str1= b[0:2]+a[2:]
str2= a[0:2]+b[2:]
str3=str1+" "+str2
print(str3)
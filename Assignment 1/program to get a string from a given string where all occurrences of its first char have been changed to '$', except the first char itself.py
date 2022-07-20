#Q4.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
c="election"
first=c[0]
c=c.replace(c[0],"$")
print(first+c[1:])
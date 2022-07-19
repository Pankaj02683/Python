#Q11
str=input("Enter string\n")
for i in range(len(str)):
    if i%2==0:
        print(str[i],end=" ")
        i=i+1
    else:
        i=i+1
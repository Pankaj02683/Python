#Q6
str=input("Enter string\n")
if len(str)<3:
    print(str)
elif(str.endswith("ing")):
    print(str+"ly")
else:
    print(str+"ing")
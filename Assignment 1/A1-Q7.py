#Q7
str=input("Enter string\n")
pos_not=str.find("not")
pos_poor=str.find("poor")
# print(str.find("not"))
# print(str.find("poor"))

if pos_poor>pos_not and pos_not>0 and pos_poor>0:
    str=str.replace(str[pos_not:pos_poor+4],"good")
    print(str)
else:
    print(str)
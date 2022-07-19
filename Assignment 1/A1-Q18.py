#Q18
def str3char(str):
    if len(str)<3:
        print(str)
    else:
        print(str[0:3])

str=input("enter string or word")
print(str3char(str))
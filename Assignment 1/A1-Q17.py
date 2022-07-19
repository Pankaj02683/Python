#Q17
def copy(str):
    if len(str)<2:
        print("invalid string")
    else:
        return (str[-2:]*4)

str=input("enter string or word")
print(copy(str))
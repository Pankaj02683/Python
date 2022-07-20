#Q23
def str_checker(str):
    char=input("enter the character you want to check\n")
    if str.startswith(char):
        return "yes"
    else:
        return "no"

str=input("enter the string\n")
print(str_checker(str))
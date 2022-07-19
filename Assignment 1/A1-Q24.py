#Q24
def starts_with(str, char):
    if str.startswith(char):
        return True
    else:
        return False

str = input("enter a string ")
my_char = input("enter a character ")
print(starts_with(str, my_char))
#Q21
def func(str):
    str_up =0
    for letter in str[0:4]:
        if letter.upper()==letter:
            str_up+=1
    if str_up>=2:
        return str.upper()
    return str
        
print(func("hello"))
print(func("heLLo"))
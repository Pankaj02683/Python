#Q19
def last_part(str, char):
    position = str.rfind(char)
    return str[:position]

print(last_part('https://www.w3resource.com/python', "/"))
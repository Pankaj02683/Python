#Q9
c="Mango"
n=int(input("Enter the index\n"))
if(n>(len(c)-1)):
    print("invalid index")
else:
    print(c.replace(c[n],""))
#Q8
items=input("Enter the item\n")
longest=0
for item in items.split():
    if(len(item)>longest):
        longest=len(item)
        word=item
print("The longest word is", word, " with length ", longest)
#Q15
def tags(tag, text):
    return "<"+tag+">"+text+"<"+tag+">"

print (tags('i', 'Python'))
print(tags('b', 'Python Tutorial'))
print("To check if a set is subset of another set:")
def check_subset(s,S):
    if(s.issubset(S)):
        print(s ,"is a subset of ", S)
    else:
        print(s ,"is not a subset of ", S)
a={1,5,16,56}
print(a)
b={1,5,16,56,85}
print(b)
check_subset(a,b)
print()
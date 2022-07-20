print("To remove a empty tuple from list of tuples:")
def Remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
tuples=[('Sumit'),(),('yash'),('suhszz'),()]
print(Remove(tuples))
print()
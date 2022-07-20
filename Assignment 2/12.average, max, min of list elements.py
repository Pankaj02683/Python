print("To find min,average,max of a list:")
l=[45,89,1,5,111]
print(l)
print("minimum element is ",min(l))
print("maximum element is ",max(l))
print("length=",len(l))
sum=0
for i in range(0,len(l)):
    sum+=l[i]
print("sum=",sum) 
print("average element is ",sum/len(l))
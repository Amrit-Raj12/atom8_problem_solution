n=int(input("Enter number of students: "))
arr=input("Enter names: ").split()
dict={}
for i in arr:
    x = i.lower();
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
for i in dict:
    print(i,dict[i])

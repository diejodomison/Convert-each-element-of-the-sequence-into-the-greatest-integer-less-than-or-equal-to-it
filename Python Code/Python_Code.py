x=(input()).split()
m=1
k=[]
for i in x:
    m=float(i)
    k.append(int(m))
for j in k:
    if j!=k[-1]:
        print(j, end=',')
    else:
        print(j)


    



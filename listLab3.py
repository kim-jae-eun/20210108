listnum=[10,5,7,21,4,8,18]
n,m=0,0
for i in listnum:
    if i<n or n==0:
        n=i
    if i>m or m==0:
        m=i
print('최솟값 : ',n,', 최댓값 : ',m,sep='')
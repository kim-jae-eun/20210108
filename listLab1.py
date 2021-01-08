#방법 1
listnum=[10,5,7,21,4,8,18]
n=0
for i in listnum:
    if i>n:
        n=i
print('최댓값 :',n)

#방법 2
listnum=[10,5,7,21,4,8,18]
for i in listnum:
    if i>=listnum[0] and i>=listnum[1] and i>=listnum[2] and i>=listnum[3] and i>=listnum[4] and i>=listnum[5] and i>=listnum[6]:
        print('최댓값 :',i)
    else:
        continue

#방법 3 (제어문 X)
listnum=[10,5,7,21,4,8,18]
listnum.sort()
print('최댓값 :',listnum[-1])

#방법 4 (제어문 X)
listnum=[10,5,7,21,4,8,18]
listnum.sort(reverse=True)
print('최댓값 :',listnum[0])
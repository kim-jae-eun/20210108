# 1~50 사이의 난수를 10개 추출하여 listnum 에 추출 순서대로 저장
import random
listnum=[]
for i in range(10):
    a=random.randint(1,50)
    listnum.append(a)
print(listnum,'\n')

# 리스트에서 10보다 작은 값들은 100으로 변경한다.
for i in range(10):
    if listnum[i]<10:
        listnum[i]=100
print(listnum,'\n')

# 첫 번째 데이터
print(listnum[0],'\n')

# 마지막 데이터
print(listnum[-1],'\n')

# 두 번째부터 여섯 번째
print(listnum[1:6],'\n')

# 역순
print(listnum[9::-1],'\n')

# 모두
print(listnum[0:],'\n')

# 5번째 데이터 삭제
del listnum[4]
print(listnum[0:],'\n')

# 2~3번째 데이터 삭제
listnum[1:3]=[]
print(listnum[0:])
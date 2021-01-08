def sumAll(*p):
    sum,count=0,0
    for i in p:
        if type(i)==int:
            count+=1
            sum+=i
    if len(p)==0 or count==0:
        sum=None
    return sum
#예시
print(sumAll(1,2,3,4,5,6,7,8,9,10))
print(sumAll(2,5,'지우개'))
print(sumAll())
print(sumAll('물고기','지우개','연필'))
print(sumAll(1,-1))
def sumEven1(*p):
    if len(p)==0:
        sum=-1
    elif min(p)<1:
        sum='수행 불가: 1 이상의 값만 입력하세요.'
    else:
        sum=0
        for i in p:
            if i%2==0:
                sum+=i
    return sum
#예시
print(sumEven1(1,2,3,4,5,6))
print(sumEven1(5,7,9))
print(sumEven1())
print(sumEven1(2,4,5,0))
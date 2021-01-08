def print_triangle_withdeco(num,deco='%'):
    if 1<=num<=10:
        for i in range(1,num+1):
            print(' '*(num-i),deco*i,sep='')
#예시
print_triangle_withdeco(2)
print_triangle_withdeco(5,'*')
print_triangle_withdeco(11)
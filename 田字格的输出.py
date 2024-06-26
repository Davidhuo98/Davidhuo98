n = eval(input('请输入一个奇数：'))
a,b,c,d = '－','┼','∣',' '
m = n//2
if n%2 == 1:
    for i in range(n):
        if i in [0,m,n-1]:
            print('{0}{1}{0}{1}{0}'.format(b,a*m))
        else:
            print('{0}{1}{0}{1}{0}'.format(c,d*2*m))
else:
    print('输入的不是奇数')
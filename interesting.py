start_n = 1000
end_n = 10000

def test(a):
    c=0
    while (a!=0 and c<100):
        b=int(str(abs(a))[::-1])
        if(a>0):
            a=a-b
        elif (a<0):
            a=a+b
        c=c+1
    if (a==0):
        return 1
    else:
        return 0
    
for i in range(start_n, end_n):
    if (test(i)==0):
        print (str(i))
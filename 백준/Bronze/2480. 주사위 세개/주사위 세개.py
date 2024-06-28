a,b,c=list(map(int,input().split()))

if a==b and b==c and c==a:
    print (10000+1000*a)
elif a==b and a!=c:
    print (1000+100*a)
elif b==c and b!=a:
    print (1000+100*b)
elif c==a and c!=b:
    print (1000+100*c)
else:
    max_value=max(a,b,c)
    print (100*max_value)
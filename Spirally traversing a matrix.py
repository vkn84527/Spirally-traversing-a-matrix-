for _ in range(int(input())):
    m,n=map(int,input().split())
    k=list(map(int,input().split()))
    a=[]
    b=[]
    p=0
    for i in range(m):
        for j in range(n):
            a.append(k[p])
            p+=1
        b.append(a)
        a=[]
    #print(b)
    res=[]
    ab=0
    while (len(b)!=0 and len(b[0])!=0):
        if (ab%4==0):
            res+=b.pop(0)
        if(ab%4==1):
            for i in range(len(b)):
                res.append(b[i].pop())
        if(ab%4==2):
            res+=b.pop()[::-1]
        if(ab%4==3):
            for i in range(len(b))[::-1]:
                res.append(b[i].pop(0))
        ab+=1
    print(*res)
                
            
    
        

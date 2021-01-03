for _ in range(int(input())):
    [N,K,D] = list(map(int,input().split()))
    if N>=1<=100:
        a= sum(list(map(int,input().split())))
        if a<K:
            val= 0
        elif a//K!=0 and a//K<D:
            val = a//K
        elif a//K>=D:
            val=D
    print(val)
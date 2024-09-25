N,M = map(int,input().split())
basket=[]
for v in range(1,N+1):
    basket.append(v)
for _ in range(M):
    i, j = map(int, input().split())
    a = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = a
print(" ".join(map(str, basket)))
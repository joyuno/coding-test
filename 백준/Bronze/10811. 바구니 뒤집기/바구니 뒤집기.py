N,M = map(int, input().split())
basket= [x for x in range(1,N+1)]
for v in range(M):
    i,j = map(int, input().split()) 
    basket[i-1:j] = basket[i-1:j][::-1]#list[start:end:step]
print(" ".join(map(str,basket)))  
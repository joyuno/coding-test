N,M = map(int,input().split())
basket=[0]*N
for _ in range(M):
    i,j,k = map(int,input().split())
    basket[i-1:j] = [k]*(j-i+1)
for num in basket:
    print(num ,end=" ")  
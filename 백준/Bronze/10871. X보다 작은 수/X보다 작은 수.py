X,N = map(int, input().split())
numbers=list(map(int,input().split()))
if len(numbers) == X:
    for i in range(X):
        if numbers[i]<N:
            print(numbers[i], end=" ")
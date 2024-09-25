T = int(input())
numbers=[]
numbers=list(map(int,input().split())) 
if len(numbers)== T:
    print(min(numbers),max(numbers))
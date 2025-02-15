n, m = tuple(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(input())
    
k = int(input())

max_cnt = 0

for col in range(n):
    # 0의 개수 세기
    zero_count = 0
    for num in lst[col]:
        if num == '0':
            zero_count += 1
        
    # 이 행과 똑같은 값을 가진 행의 개수 세기
    col_light_cnt = 0
    if zero_count <= k and zero_count%2 == k%2:  # 이 행을 모두 킬 수 있다면
        for col2 in range(n):  
            if lst[col] == lst[col2]: 
                col_light_cnt += 1  
                
    max_cnt = max(max_cnt, col_light_cnt)  # 최대값보다 크면 업데이트
    
print(max_cnt)
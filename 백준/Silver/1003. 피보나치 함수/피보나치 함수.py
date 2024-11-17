def fibonacci_count(n):
    dp = [(1, 0), (0, 1)]  
   
    for i in range(2, n + 1):
        zero_count = dp[i - 1][0] + dp[i - 2][0]
        one_count = dp[i - 1][1] + dp[i - 2][1]
        dp.append((zero_count, one_count))

    return dp

# 입력 처리
T = int(input())  
test_cases = [int(input()) for _ in range(T)]

max_n = max(test_cases)
dp = fibonacci_count(max_n)

for n in test_cases:
    print(dp[n][0], dp[n][1])
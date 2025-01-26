def count_prime_sum(N):
    answer = 0
    Max = 4000001

    # 소수 판별 (에라토스테네스의 체)
    is_prime = [True] * Max
    is_prime[0], is_prime[1] = False, False
    primes = []

    for num in range(2, Max):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * 2, Max, num):
                is_prime[multiple] = False

    # 누적 합 배열 생성
    prefix_sum = [0]
    for prime in primes:
        prefix_sum.append(prefix_sum[-1] + prime)

    # 투 포인터를 이용한 소수의 합 계산
    left, right = 0, 1
    while right < len(prefix_sum):
        current_sum = prefix_sum[right] - prefix_sum[left]

        if current_sum < N:
            right += 1
        elif current_sum == N:
            answer += 1
            right += 1
        else:
            left += 1

    return answer


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    print(count_prime_sum(N))

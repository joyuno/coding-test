import math

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 신기한 소수 찾기 (백트래킹)
def find_magic_primes(n, current):
    if len(str(current)) == n:
        print(current)
        return

    for digit in range(1, 10):
        new_number = current * 10 + digit
        if is_prime(new_number):
            find_magic_primes(n, new_number)

# 입력
N = int(input())

# 1자리 소수부터 시작 (한 자리 소수: 2, 3, 5, 7)
for prime in [2, 3, 5, 7]:
    find_magic_primes(N, prime)

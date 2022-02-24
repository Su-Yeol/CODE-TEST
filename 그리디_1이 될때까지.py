import time

start_time = time.time()

n, k = map(int, input().split())
result = 0

while True:
  # N = K로 나누어떨어지는 수가 될때까지 1 빼기
  target = (n // k) * k  # target = k로 나누어 떨어지는 수
  result += n-target  # 1을 몇 번 빼기했는지
  n = target

  if n < k:
    break

  # k로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

end_time = time.time()
print("Time: ", end_time-start_time)
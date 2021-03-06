import time

start_time = time.time()

n = int(input())  # 모험가의 수
data = list(map(int, input().split()))  # 공포도
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모함가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모함가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)

end_time = time.time()
print("Time: ", end_time-start_time)
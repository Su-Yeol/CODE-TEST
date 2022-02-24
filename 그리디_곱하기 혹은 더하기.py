array = [i for i in range(10)]

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1' 인 경우, 곱하기보다는 더하기 수행
    num = int(data[1])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

end_time = time.time()
print("Time: ", end_time-start_time)
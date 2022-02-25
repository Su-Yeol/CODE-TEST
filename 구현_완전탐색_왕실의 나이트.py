input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1  # 1부터 시작이기 때문에 +1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
result = 0

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면
    if next_column >= 1 or next_row >= 1 or next_row <= 8 or next_column <= 8:
        result += 1

print(result)

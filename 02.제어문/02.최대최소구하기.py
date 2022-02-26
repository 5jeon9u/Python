numbers = [7, 10, 22, 4, 3, 17]
# (1) 초기값을 주어진 자료값들 보다 작은 값으로 설정하는 경우
max_val = 0
for val in numbers:
    if max_val < val:
        max_val = val
print(max_val)

# (2) 초기값을 주어진 자료값의 첫 값으로 설정하는 경우
max_val = numbers[0]
for val in numbers:
    if max_val < val:
        max_val = val
print(max_val)

# (3) 최대(최소)값의 위치 구하기
max_idx = 0
for i in range(1, len(numbers)):
    if numbers[max_idx] < numbers[i]:
        max_idx = i
print(max_idx, numbers[max_idx])
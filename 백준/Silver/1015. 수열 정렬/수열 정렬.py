n = int(input())
input_list = list(map(int, input().split()))

# 수열의 인덱스 속성 추가 (2차원 배열)
unsorted_list = [[item, i] for i, item in enumerate(input_list)]

# unsorted_list의 각 요소에서 인덱스 0을 기준으로 내림차순 정렬
sorted_list = sorted(unsorted_list, key=lambda x: x[0])

result = [0] * n
# 정렬된 리스트의 각 요소의 인덱스 1의 값을 가져와서 result[해당 값]에 현재 순서를 입력
for i, item in enumerate(sorted_list):
    result[item[1]] = i

for num in result:
    print (num, end=' ')
#선택 정렬
array = [5,7,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index],array[i]
print(array)


#삽입 정렬
##시간 복잡도:O(N^2), 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작합니다. 
for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j] <array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break
print(array)


#퀵 정렬: 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
#시간 복잡도: 평균 O(NlogN) 최악의 경우 O(N^2), 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬 수행 시,O(N^2)
#표준라이브러리는 기본적으로 NlogN 유지

def quick_sort(array, start,end):
    if start>= end:
        return
    pivot = start
    left = start+1
    right = end
    while (left <= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <=  end and array[left] <= array[pivot]):
            left +=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -=1
        if(left>right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)

print(array)

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) +[pivot] + quick_sort(right_side)
print(quick_sort(array))

# 계수정렬
# 특정한 조건이 부합할 때만 사용/ 매우 빠르게 동작
# 데이터 개수가 N , 데이터(양수) 중 최댓값이 K일 때, 최악의 경우에도 수행시간 O(N+K) 보장
# 공간 복잡도, 시간 복잡도는 모두 O(N+K)

# 1. min-max 범위 담긴 리스트 생성 (인덱스: count 개수)
# 2. 각 인덱스에 해당하는 값만큼 확인하여 출력


#모든 원소의 값이 0 보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,1,9,1,4,8,0,5,2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end = ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력


# 문제1 (진행 중)
N, K = map(int, input().split(' '))
A = list(input().split(" "))
B = list(input().split(" "))

A.sort()
B.sort(reverse= True)
print(B)

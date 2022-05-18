#선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]
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

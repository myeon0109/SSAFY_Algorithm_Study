#6-5 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array)<=1:
    return array
  pivot = array[0]# pivot -> 교환하기 위한 기준
  tail = array[1:]#피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]# 분할된 왼쪽 부분
  right_side = [x for x in tail if x>pivot]# 분할된 오른쪽 부분
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

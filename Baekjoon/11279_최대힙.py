# class MaxHeap:
#
#     def __init__(self):
#         self.data = [0] #힙에선 0번 인덱스 사용 X
#
#     def Hpush(self, item):
#         self.data.append(item)
#
#         lastIdx = len(self.data) - 1
#         child = lastIdx
#         parent = lastIdx // 2
#
#         while parent > 0: # 부모가 root를 넘어가지 않음
#             if  self.data[child] > self.data[parent]: # 자식이 부모보다 크면
#                 # 부모와 자식 바꿔줌
#                 self.data[child], self.data[parent] = self.data[parent], self.data[child]
#             child = parent #자식은 기존의 부모로 해서 트리를 올라감
#             parent = child // 2 #바꿔준 자식의 부모를 다시 할당
#
#     def Hpop(self):
#         if len(self.data) > 1: #힙에 데이터가 있는 경우
#             #가장 끝에 값과 루트를 바꿔줌 (힙은 트리의 가장 마지막 인덱스에서만 삽입 삭제가 가능하기 때문)
#             self.data[1], self.data[-1] = self.data[-1], self.data[1]
#             value = self.data.pop() #가장 마지막 값으로 바꿔준 기존의 루트를 뽑아냄
#             self.maxHeapify(1) #재정렬
#         else: # 힙에 아무것도 없을 경우
#             value = 0
#         return value
#
#     def maxHeapify(self, root): # 인자로 받는 root 부터 root의 값과 자식들을 비교하며 재정렬
#         l_child = 2 * root
#         r_child = (2 * root) + 1
#         max_vertex = root #큰 값을 담을 변수, root로 초기화 (root부터 시작이니까)
#         #왼쪽 자식이 존재하고 root보다 왼쪽 자식이 더 클경우
#         if l_child < len(self.data) and self.data[root] < self.data[l_child]:
#             max_vertex = l_child #최대값 변수에 왼쪽 자식 넣어줌
#         #왼쪽이 있더라도 오른쪽이 있으면 오른쪽으로 바꿔줌
#         if r_child < len(self.data) and self.data[root] < self.data[r_child]:
#             max_vertex = r_child
#         #만약 root보다 자식이 더 커서 max_vertext가 바뀌었으면 둘의 위치를 바꿔줌
#         if max_vertex != root:
#             self.data[root], self.data[max_vertex] = self.data[max_vertex], self.data[root]
#             self.maxHeapify(max_vertex) #새로운 root부터 다시 함수 호출해서 정렬
#
# import sys
#
# N = int(sys.stdin.readline())
# heap = MaxHeap()
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         value = heap.Hpop()
#         print(value)
#     else:
#         heap.Hpush(num)

import heapq, sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap):
            value = -heapq.heappop(heap)
            print(value)
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)
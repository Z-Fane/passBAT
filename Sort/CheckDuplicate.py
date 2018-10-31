# -*- coding:utf-8 -*-
class HeapSort:
    def heapSort(self, A, n):
        # write code here
        # 构建大根堆
        for i in range((n -2)//2,-1,-1):
            self.adjust_heap(A,n,i)
        # 调整堆结构
        for j in range(n-1,-1,-1):
            A[0], A[j] = A[j], A[0]
            self.adjust_heap(A, j ,0)
        return A
    def adjust_heap(self,heap,HeapSize,root):
        left = 2 * root + 1
        right = left + 1
        larger = root
        if left < HeapSize and heap[larger] < heap[left]:
            larger = left
        if right < HeapSize and heap[larger] < heap[right]:
            larger = right
        if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
            heap[larger], heap[root] = heap[root], heap[larger]
            self.adjust_heap(heap, HeapSize, larger)
class Checker:
    def checkDuplicate(self, a, n):
        HeapSort().heapSort(a,n)
        for i in range(1,n):
            if a[i]==a[i-1]:
                return True
        return False
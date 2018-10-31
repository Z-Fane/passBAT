class ScaleSort:

    def sortElement(self, A, n, k):
        # 构建k个数的小根堆
        heap = self.build_heap(A[:k], k)
        # 弹出小根堆的堆顶。
        for i in range(k, n):
            A[i - k], heap[0] = heap[0], A[i]  # 取出最小值，依次赋值给A数组
            self.adjust_heap(heap, k, 0)
        # 后面的k个数即是数组的最大的k个数
        for i in range(n - k, n):
            A[i] = heap[0]
            heap[0], heap[k - 1] = heap[k - 1], heap[0]
            k -= 1
            self.adjust_heap(heap, k, 0)
        return A

    def build_heap(self, A, heap_size):
        # 构建小根堆
        for i in range((heap_size) // 2 - 1, -1, -1):
            self.adjust_heap(A, heap_size, i)
        return A

    def adjust_heap(self, A, size, i):
        left = i * 2 + 1
        while left < size:
            if left + 1 < size and A[left + 1] < A[left]:
                left += 1
            if A[i] < A[left]:
                break
            A[i], A[left] = A[left], A[i]
            i, left = left, left * 2 + 1
class MergeSort:
    def mergeSort(self, A, n):
        self.partition(A, 0, n - 1)
        return A

    def partition(self, A, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.partition(A, l, mid)
        self.partition(A, mid + 1, r)
        self.merge(A, l, mid, r)

    def merge(self, A, l, mid, r):
        tmp = [0 for i in range(r - l + 1)]
        i = 0
        p1 = l
        p2 = mid + 1
        while (p1 <= mid and p2 <= r):
            if A[p1] < A[p2]:
                tmp[i] = A[p1]
                p1 += 1
            else:
                tmp[i] = A[p2]
                p2 += 1
            i += 1

        while (p1 <= mid):
            tmp[i] = A[p1]
            p1 += 1
            i += 1
        while (p2 <= r):
            tmp[i] = A[p2]
            p2 += 1
            i += 1
        for i in range(len(tmp)):
            A[l + i] = tmp[i]
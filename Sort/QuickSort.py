def quickSort(self, A, n):
    self.quick_sort(A, 0, n - 1)
    return A


def quick_sort(self, A, l, r):
    if l < r:
        less, more = self.partition(A, l, r)
        self.quick_sort(A, l, less)
        self.quick_sort(A, more, r)


def partition(self, A, l, r):
    less = l - 1
    more = r
    while l < more:
        if A[r] < A[l]:
            more -= 1
            self.swap(A, l, more)
        elif A[r] > A[l]:
            less += 1
            self.swap(A, l, less)
            l += 1
        else:
            l += 1
    self.swap(A, more, r)
    return less, more + 1


def swap(self, A, l, r):
    tmp = A[l]
    A[l] = A[r]
    A[r] = tmp
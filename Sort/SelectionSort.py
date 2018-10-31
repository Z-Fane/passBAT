class SelectionSort:
    def selectionSort(self, A, n):
        for i in range(n):
            min_i=i
            for j in range(i+1,n):
                if A[min_i]>A[j]:
                    min_i=j
            tmp=A[i]
            A[i]=A[min_i]
            A[min_i]=tmp
        return A
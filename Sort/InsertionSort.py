class InsertionSort:
    def insertionSort(self, A, n):
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if A[j]>A[j+1]:
                    tmp=A[j]
                    A[j]=A[j+1]
                    A[j+1]=tmp
        return A
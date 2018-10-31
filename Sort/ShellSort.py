class ShellSort:
    def shellSort(self, A, n):
        # write code here
        step=n//2
        while step>0:
            for i in range(step,n):
                while i>=step and A[i-step] >A[i]:
                    A[i],A[i-step]=A[i-step],A[i]
                    i-=step
            step=step//2
        return A
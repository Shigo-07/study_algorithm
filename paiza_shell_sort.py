N = 5
*A, = [5,6,9,2,3]

gap = N // 2
while gap > 0:
    for i in range(gap,N):
        temp = A[i]
        j = i
        while j >= gap and A[j-gap] > temp:
            A[j] = A[j-gap]
            j -= gap
        A[j] = temp
    gap //= 2

print(A)
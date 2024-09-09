N = int(input())
*A, = map(int,input().split())



print(" ".join(map(str,A)))
for i in range(1,N):
    temp = A[i]
    j = i - 1
    while j >= 0 and A[j] > temp:
        A[j + 1] = A[j]
        j -= 1
    A[j+1] = temp
    print(" ".join(map(str,A)))

N = int(input())
*A, = map(int,input().split())
count = 0

for i in range(N):
    min_index = i
    for j in range(i+1,N):
        if A[min_index] > A[j]:
            min_index = j
    
    if min_index != i:
        A[min_index],A[i] = A[i],A[min_index]
        count += 1

print(" ".join(map(str,A)))
print(count)
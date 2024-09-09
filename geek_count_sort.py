N = 13
S = "geeksforgeeks"


counts = [0] * 26
result = [None] * N

for i in S:
    counts[ord(i) - ord("a")] +=1

for i in range(1,len(counts)):
    counts[i] += counts[i - 1]

for i in S:
    index = counts[ord(i) - ord("a")]
    result[index - 1] = i
    counts[ord(i) - ord("a")] -= 1

print("".join(result))

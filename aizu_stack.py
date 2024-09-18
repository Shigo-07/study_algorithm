# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_A
# input = "1 2 + 3 4 - *"
input = input()
list = input.split()
stack = []
for i in list:
    if i == "+":
        sum = stack.pop() + stack.pop()
        stack.append(sum)
    elif i == "-":
        div = -(stack.pop() - stack.pop())
        stack.append(div)
    elif i == "*":
        ans = stack.pop() * stack.pop()
        stack.append(ans)
    else:
        stack.append(int(i))

print(stack.pop())


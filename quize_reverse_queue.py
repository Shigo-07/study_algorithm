from collections import deque
def reverse(queue):
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    

if __name__ == "__main__":
    d = deque()
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    print(d)
    q = reverse(q)
    print(q)

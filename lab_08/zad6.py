from collections import deque, Counter

def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())

print(create_kolo_fortuny(2,1,4,'yo'))
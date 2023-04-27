from timeit import timeit

setup_deq = """
from collections import deque
queue = deque('dvpa'.split())
"""
stmt1_deq="""
for x in range(100_000_000):
    queue.append('B')
"""
stmt2_deq="""
for x in range(100_000_000):
    queue.appendleft('A')
"""
setup_list = """
lista = 'dvpa'.split()
"""
stmt1_list="""
for x in range(100_000_000):
    lista.append('B')
"""
stmt2_list="""
for x in range(100_000_000):
    lista.insert(0,'A')
"""
print('tile of append in deq: ', timeit(stmt1_deq, setup_deq, number=100))
print('tile of append left in deq: ', timeit(stmt2_deq, setup_deq, number=100))
print('tile of append in list: ', timeit(stmt1_list, setup_list, number=100))
print('tile of append "left" in list: ', timeit(stmt2_list, setup_list, number=100))
from timeit import timeit
import random
setup = """
from array import array
import random
"""
stmt1 = """
tab_of_ints = array('i', [random.randint(0, 1_000_000) for _ in range(1_000_000)])
"""
stmt2 = """
tab_of_longs = array('q', [random.randint(0, 1_000_000) for _ in range(1_000_000)])
"""
stmt3 = """
list_of_ints = [random.randint(0, 1_000_000) for _ in range(1_000_000)]
"""


print('tab of ints: ', timeit(stmt1, setup, number=100))
print('tab of longs: ',timeit(stmt2, setup, number=100))
print('list of ints: ',timeit(stmt3, setup, number=100))

# tab of ints:  134.5199028000061
# tab of longs:  139.2769380999962
# list of ints:  135.58394159999443
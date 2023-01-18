import random

from BinarySearch import BinarySearch

len_test = 10
TestList = sorted(random.sample(range(0, 100), len_test))
Target_index = random.randint(0, len_test-1)
Target = TestList[Target_index]
print(TestList, Target, Target_index)

assert(BinarySearch(TestList, Target), Target_index)
# BinarySearch([1, 30, 13, 46, 3, 17, 52, 128 ])

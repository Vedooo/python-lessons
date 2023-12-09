from functools import cached_property
import time

class ExpensiveComputation:

    def __init__(self, value):
        self.value = value

    @cached_property # it's gonna cached steps for example print line will add cache.
    def computation_result(self):
        print('Calculating result..')
        time.sleep(3)
        return self.value * 5

ec = ExpensiveComputation(10)

print(ec.computation_result)
print(ec.computation_result)
print(ec.computation_result)

# Calculating result..
# 50
# 50
# 50


ec.value = 100

print(ec.computation_result)

del ec.computation_result # we delete the cached value

print(ec.computation_result)

# Calculating result..
# 500
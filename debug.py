# Debugging
# TODO: https://www.geeksforgeeks.org/differences-between-testing-and-debugging/
# Bug means program has fault or error.
# Debugging is the process to correct the bugs found during testing.
# Debugging is based on different types of bugs.

# Testing is the process to find bugs and errors.
# It is based on different testing levels i.e. unit testing, integration testing, system testing etc.

def add_num(a, b):
    s = int(a)+int(b)
    return s


n1 = input('enter first no:')
n2 = input("enter second no:")

s = add_num(n1, n2)
print('sum is: ', s)

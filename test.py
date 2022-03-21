from main import *

def TEST1():
    return DivisibleBy7(7)

def TEST2():
    return DivisibleBy7(15)

TEST1()

if TEST2():
    pass
else:
    exit(1)
from math import log
def calculate_logarithm(number, log_base):
    result = None
    if base == 'natural':
        result = log(number)
    else:
        result = log(number, log_base)
    return result

num = int(input())
base = input()

print(f"{calculate_logarithm(num,int(base)):.2f}")

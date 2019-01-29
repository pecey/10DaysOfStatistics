import functools
import math

def main():
    n = input()
    numbers = map(int, raw_input().split())
    mean_of_numbers = mean(numbers)
    squared_distance_from_mean = map(lambda x: (x - mean_of_numbers)**2, numbers)
    squared_sum = sum(squared_distance_from_mean)
    standard_deviation = math.sqrt(squared_sum/float(n))
    print(standard_deviation)

def sum(numbers):
    return functools.reduce(lambda a,b: a + b, numbers)

def mean(numbers):
    return sum(numbers)/float(len(numbers))

if __name__ == "__main__":
    main()
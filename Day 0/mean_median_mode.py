import functools

def main():
    n = input()
    n_numbers = map(int, raw_input().split())
    n_numbers.sort()
    print("{:.1f}".format(mean(n_numbers, n)))
    print("{:.1f}".format(median(n_numbers)))
    print(mode(n_numbers))


def mean(n_numbers, size):
    return functools.reduce(lambda a,b: a+b, n_numbers)/float(size)

def median(n_numbers, size):
    if size % 2 == 1:
        return n_numbers[size/2]
    else:
        return (n_numbers[size/2] + n_numbers[(size/2) - 1])/float(2)

def mode(n_numbers):
    highest_count = 0
    mode = -1
    numbers_with_count = {}
    for number in n_numbers:
        if number in numbers_with_count.keys():
            numbers_with_count[number] = numbers_with_count[number] + 1
        else:
            numbers_with_count[number] = 1

        if highest_count < numbers_with_count[number]:
            highest_count = numbers_with_count[number]
            mode = number

    return mode

if __name__ == "__main__":
    main()
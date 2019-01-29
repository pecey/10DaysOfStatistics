def main():
    n = input()
    numbers = map(int, raw_input().split())
    frequency = map(int, raw_input().split())
    dataset = [item for sublist in map(construct_dataset, numbers, frequency) for item in sublist]
    dataset.sort()
    q1,q2,q3 = quartiles(dataset)

    print("{:.1f}".format(q3-q1))

def construct_dataset(number_as_string, frequency):
    partial = []
    for i in range(frequency):
        partial.append(number_as_string)
    return partial

def quartiles(numbers):
    n = len(numbers)
    q1 = median(numbers[:(n/2)])
    if n % 2 == 1:
        q2 = numbers[n/2]
        q3 = median(numbers[(n/2)+1:])
    else:
        q2 = (numbers[n/2] + numbers[(n/2)-1])/float(2)
        q3 = median(numbers[(n/2):])

    return (q1,q2,q3)


def median(sorted_numbers):
    size = len(sorted_numbers)
    if size % 2 == 0:
        return (sorted_numbers[size/2] + sorted_numbers[(size/2) - 1])/float(2)
    else:
        return sorted_numbers[size/2]

if __name__ == "__main__":
    main()
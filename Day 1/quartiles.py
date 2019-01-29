def main():
    n = input()
    numbers = map(int, raw_input().split())
    numbers.sort()
    q1 = median(numbers[:(n/2)])
    if n % 2 == 1:
        q2 = numbers[n/2]
        q3 = median(numbers[(n/2)+1:])
    else:
        q2 = (numbers[n/2] + numbers[(n/2)-1])/float(2)
        q3 = median(numbers[(n/2):])

    print(q1)
    print(q2)
    print(q3)

def median(sorted_numbers):
    size = len(sorted_numbers)
    if size % 2 == 0:
        return (sorted_numbers[size/2] + sorted_numbers[(size/2) - 1])/float(2)
    else:
        return sorted_numbers[size/2]

if __name__ == "__main__":
    main()
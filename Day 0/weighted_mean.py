def main():
    n = input()
    n_numbers = map(int, raw_input().split())
    weights = map(int, raw_input().split())

    print("{:.1f}".format(weighted_mean(n_numbers, weights, n)))

def weighted_mean(n_numbers, weights, size):
    sum = 0
    weight_sum = 0
    for index in range(size):
        sum = sum + (n_numbers[index] * weights[index])
        weight_sum = weight_sum + weights[index]
    return float(sum)/weight_sum

if __name__ == "__main__":
    main()
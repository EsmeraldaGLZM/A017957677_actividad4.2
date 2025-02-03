import sys

import time


def read_numbers_from_file(filename):
    """Reads a file and extracts valid numeric values, ignoring invalid lines."""
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid data: {line.strip()} - Skipping")
    return numbers


def compute_mean(numbers):
    """Computes the mean manually without sum() or len()."""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count if count > 0 else 0


def manual_sort(numbers):
    """Implements a basic Bubble Sort algorithm to sort numbers."""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def compute_median(numbers):
    """Computes the median manually without using sorted()."""
    sorted_numbers = manual_sort(numbers[:])
    n = len(sorted_numbers)
    mid = n // 2
    return sorted_numbers[mid] if n % 2 != 0 else (
        sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


def compute_mode(numbers):
    """Computes the mode manually without max() or dictionary methods."""
    frequency = []
    values = []  
    for num in numbers:
        if num in values:
            index = values.index(num)
            frequency[index] += 1
        else:
            values.append(num)
            frequency.append(1)   
    max_freq = 0
    modes = []
    for i, freq in enumerate(frequency):
        if freq > max_freq:
            max_freq = freq
            modes = [values[i]]
        elif freq == max_freq:
            modes.append(values[i])   
    return modes if len(modes) > 1 else modes[0]


def compute_variance(numbers, mean):
    """Computes variance manually without sum()."""
    total = 0
    count = 0
    for num in numbers:
        total += (num - mean) ** 2
        count += 1
    return total / count if count > 0 else 0


def compute_std_dev(variance):
    """Computes standard deviation manually."""
    return variance ** 0.5


def write_results(filename, mean, median, mode, variance, std_dev, elapsed_time):
    """Writes the calculated statistics and execution time to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Mean: {mean}\n")
        file.write(f"Median: {median}\n")
        file.write(f"Mode: {mode}\n")
        file.write(f"Variance: {variance}\n")
        file.write(f"Standard Deviation: {std_dev}\n")
        file.write(
            f"Execution Time: {elapsed_time:.6f} seconds\n"
        )


def main():
    """Main function to read a file, compute statistics, and display results."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = "StatisticsResults.txt"
    start_time = time.time()
    numbers = read_numbers_from_file(input_filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)
    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_std_dev(variance)
    elapsed_time = time.time() - start_time 
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Execution Time: {elapsed_time:.6f} seconds")   
    write_results(output_filename, mean, median, mode, variance, std_dev, elapsed_time)


if __name__ == "__main__":
    main()

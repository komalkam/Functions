def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
sample_list = [8, 2, 3, 0, 7]
result = sum_numbers(sample_list)
print("Sum:", result)
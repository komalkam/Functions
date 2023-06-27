def count_upper_lower_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count
sample_string = 'The quick Brow Fox'
upper_count, lower_count = count_upper_lower_characters(sample_string)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)
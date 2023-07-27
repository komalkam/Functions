def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)

    return pairs


if __name__ == "__main__":
   
    input_array = [1, 4, 6, 8, 2, 5, 9]
    target = 10

    result_pairs = find_pairs_with_sum(input_array, target)

    if len(result_pairs) == 0:
        print("No pairs found.")
    else:
        print("Pairs with sum equal to", target, ":")
        for pair in result_pairs:
            print(pair)

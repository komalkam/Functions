def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
   
    input_array = [38, 27, 43, 3, 9, 82, 10]

    sorted_array = quick_sort(input_array)
    print("Sorted Array:", sorted_array)

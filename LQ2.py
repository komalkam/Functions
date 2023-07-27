def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == "__main__":
 
    input_array = [1, 2, 3, 4, 5]

    print("Original Array:", input_array)
    reverse_array_in_place(input_array)
    print("Reversed Array:", input_array)

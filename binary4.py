def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    
    input_array = [38, 27, 43, 3, 9, 82, 10]

    insertion_sort(input_array)
    print("Sorted Array:", input_array)

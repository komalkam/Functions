def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
 
    arr = list(map(int, input("Enter the sorted array (space-separated): ").split()))
    
    
    target_element = int(input("Enter the target element: "))

    result = binary_search(arr, target_element)
    if result != -1:
        print(f"Element {target_element} found at index {result}.")
    else:
        print(f"Element {target_element} not found in the array.")

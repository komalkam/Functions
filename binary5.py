def sort_list_of_strings_using_sorted(input_list):
    sorted_list = sorted(input_list)
    return sorted_list


def sort_list_of_strings_using_sort(input_list):
    input_list.sort()
    return input_list


if __name__ == "__main__":
    
    input_list = input("Enter the list of strings (comma-separated): ").split(',')

    input_list = [s.strip() for s in input_list]

    sorted_list1 = sort_list_of_strings_using_sorted(input_list.copy())
    print("Sorted list using sorted():", sorted_list1)


    sorted_list2 = sort_list_of_strings_using_sort(input_list.copy())
    print("Sorted list using sort():", sorted_list2)

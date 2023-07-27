def first_non_repeated_char(s):
    char_count = {}


    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

  
    for char in s:
        if char_count[char] == 1:
            return char

    
    return None


if __name__ == "__main__":
   
    input_string = input("Enter a string: ")

    result = first_non_repeated_char(input_string)
    if result:
        print("The first non-repeated character is:", result)
    else:
        print("There are no non-repeated characters in the string.")

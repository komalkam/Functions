def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False

    concatenated_string = s1 + s1
    if s2 in concatenated_string:
        return True
    else:
        return False


if __name__ == "__main__":
  
    string1 = "hello"
    string2 = "lohel"

    if are_rotations(string1, string2):
        print(f"{string1} and {string2} are rotations of each other.")
    else:
        print(f"{string1} and {string2} are not rotations of each other.")

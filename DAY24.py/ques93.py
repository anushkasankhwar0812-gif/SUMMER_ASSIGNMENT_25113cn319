#write a program to check string rotation
def is_rotation(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Concatenate str1 with itself and check if str2 is a substring
    return str2 in (str1 + str1)
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
print(is_rotation(input_str1, input_str2))


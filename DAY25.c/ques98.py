#write a program to find common characters in two strings
def find_common_characters(str1, str2):
    common_chars = []
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars.append(char)
    return ''.join(common_chars)
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
print("Common characters:", find_common_characters(input_str1, input_str2))

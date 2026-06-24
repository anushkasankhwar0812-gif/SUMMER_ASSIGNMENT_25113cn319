#write a program to remove duplicates characters from a string
def remove_duplicates(s):
    seen = set()  # Set to keep track of seen characters
    result = []   # List to store the result without duplicates
    
    # Iterate through each character in the string
    for char in s:
        if char not in seen:
            seen.add(char)  # Add the character to the seen set
            result.append(char)  # Append the character to the result list
            
    return ''.join(result)  # Join the list into a string and return
input_str = input("Enter a string: ")
print("String without duplicates:", remove_duplicates(input_str))
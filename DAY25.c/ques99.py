#write a program to sort names alphabetically
def sort_names(names):
    return sorted(names)  # Use the built-in sorted function to sort the list of names
input_names = input("Enter names separated by commas: ").split(',')  # Split input string into a list of names
sorted_names = sort_names(input_names)  # Call the sort_names function to sort the names
print("Names in alphabetical order:")
for name in sorted_names:
    print(name)
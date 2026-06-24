#write a program to find longest word in a string
def find_longest_word(s):
    words = s.split()  # Split the string into words
    longest_word = ""
    
    # Iterate through the words to find the longest one
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word
input_str = input("Enter a string: ")
longest_word = find_longest_word(input_str)
print("Longest word:", longest_word)
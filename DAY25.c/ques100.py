#write a program to sort words by length
def sort_words_by_length(words):
    return sorted(words, key=len)  # Sort the list of words based on their length

input_words = input("Enter words separated by commas: ").split(',')  # Split input string into a list of words
sorted_words = sort_words_by_length(input_words)  # Call the sort_words_by_length function to sort the words

print("Words in order of increasing length:")
for word in sorted_words:
    print(word)
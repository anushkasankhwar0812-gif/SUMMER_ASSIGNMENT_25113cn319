#write a program to compress a string
def compress_string(s):
    compressed = []
    count = 1
    
    # Iterate through the string and count consecutive characters
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
            
    # Append the last character and its count
    compressed.append(s[-1] + str(count))
    
    # Join the compressed list into a string
    compressed_str = ''.join(compressed)
    
    # Return the compressed string if it's shorter than the original, otherwise return the original
    return compressed_str if len(compressed_str) < len(s) else s
input_str = input("Enter a string to compress: ")
compressed_result = compress_string(input_str)
print("Compressed string:", compressed_result)

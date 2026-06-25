#write a program to merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    merged_array = []  # List to store the merged result
    i, j = 0, 0  # Pointers for arr1 and arr2
    
    # Iterate through both arrays until one is exhausted
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])  # Append smaller element from arr1
            i += 1  # Move pointer in arr1
        else:
            merged_array.append(arr2[j])  # Append smaller element from arr2
            j += 1  # Move pointer in arr2
            
    # If there are remaining elements in arr1, append them
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
        
    # If there are remaining elements in arr2, append them
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
        
    return merged_array  # Return the merged sorted array

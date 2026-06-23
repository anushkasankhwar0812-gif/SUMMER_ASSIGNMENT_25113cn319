//write a program to find first non-repeating character in a string.
#include <stdio.h>
int main() {
    char str[100];
    int freq[256] = {0}; // Initialize frequency array to zero
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Calculate frequency of each character
    for (int i = 0; str[i] != '\0'; i++) {
        freq[(unsigned char)str[i]]++;
    }
    
    // Find the first non-repeating character
    char firstNonRepeating = '\0';
    for (int i = 0; str[i] != '\0'; i++) {
        if (freq[(unsigned char)str[i]] == 1) {
            firstNonRepeating = str[i];
            break;
        }
    }
    
    if (firstNonRepeating != '\0') {
        printf("The first non-repeating character is: '%c'\n", firstNonRepeating);
    } else {
        printf("No non-repeating character found.\n");
    }
    
    return 0;
}
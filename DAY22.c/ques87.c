//write a program to character frequency in a string.
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
    
    // Display the frequency of characters
    printf("Character Frequency in the string:\n");
    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            printf("Character '%c' occurs %d times\n", i, freq[i]);
        }
    }
    
    return 0;
}

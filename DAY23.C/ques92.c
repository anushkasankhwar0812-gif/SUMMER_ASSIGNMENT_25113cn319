//write a progrAM to find maximum occurring character in a string.
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

    // Find the maximum occurring character
    char maxChar = '\0';
    int maxFreq = 0;
    for (int i = 0; i < 256; i++) {
        if (freq[i] > maxFreq) {
            maxFreq = freq[i];
            maxChar = (char)i;
        }
    }

    if (maxChar != '\0') {
        printf("The maximum occurring character is: '%c' with frequency %d\n", maxChar, maxFreq);
    } else {
        printf("No characters found in the string.\n");
    }

    return 0;
}
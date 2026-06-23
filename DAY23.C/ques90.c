//write a program to find first repeating character in a string.
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

    // Find the first repeating character
    char firstRepeating = '\0';
    for (int i = 0; str[i] != '\0'; i++) {
        if (freq[(unsigned char)str[i]] > 1) {
            firstRepeating = str[i];
            break;
        }
    }

    if (firstRepeating != '\0') {
        printf("The first repeating character is: '%c'\n", firstRepeating);
    } else {
        printf("No repeating character found.\n");
    }

    return 0;
}
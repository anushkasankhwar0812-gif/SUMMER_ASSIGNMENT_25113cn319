//write a program to count words in a string
#include <stdio.h>
int main() {
    char str[100];
    int wordCount = 0;
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == ' ' || str[i] == '\t' || str[i] == '\n') {
            wordCount++;
        }
    }
    
    // Increment wordCount for the last word
    wordCount++;
    
    printf("Number of words in the string: %d\n", wordCount);
    return 0;
}

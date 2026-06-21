//write a program to reverse a string.
#include <stdio.h>
int main() {
    char str[100], reversed[100];
    int length = 0;
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Calculate the length of the string
    while (str[length] != '\0') {
        length++;
    }
    
    // Reverse the string
    for (int i = 0; i < length; i++) {
        reversed[i] = str[length - i - 1];
    }
    reversed[length] = '\0'; // Null-terminate the reversed string
    
    printf("Reversed string: %s", reversed);
    return 0;
}
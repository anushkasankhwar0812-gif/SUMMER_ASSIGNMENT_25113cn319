//write a program to check pallindrome string
#include <stdio.h>
int main() {
    char str[100], reversed[100];
    int length = 0, isPalindrome = 1;
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
    
    // Check if the original string and reversed string are the same
    for (int i = 0; i < length; i++) {
        if (str[i] != reversed[i]) {
            isPalindrome = 0;
            break;
        }
    }
    
    if (isPalindrome) {
        printf("The string is a palindrome.\n");
    } else {
        printf("The string is not a palindrome.\n");
    }
    
    return 0;
}
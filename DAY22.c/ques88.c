//write a program to remove spaces from a string.
#include <stdio.h>
int main() {
    char str[100], result[100];
    int j = 0;
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove spaces from the string
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ') {
            result[j++] = str[i];
        }
    }
    result[j] = '\0'; // Null-terminate the result string
    
    printf("String after removing spaces: %s", result);
    return 0;
}
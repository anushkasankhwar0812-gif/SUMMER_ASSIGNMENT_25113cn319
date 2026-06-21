//write a program to find string length without strlen() function.
#include <stdio.h>
int main() {
    char str[100];
    int length = 0;
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    while (str[length] != '\0') {
        length++;
    }
    printf("Length of the string is: %d", length);
    return 0;
}
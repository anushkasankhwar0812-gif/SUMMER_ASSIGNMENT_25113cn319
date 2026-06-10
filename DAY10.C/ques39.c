//write a program to print character pyramid.
#include <stdio.h>
void printCharacterPyramid(int n) {
    char ch = 'A'; // Starting character
    for (int i = 1; i <= n; i++) {
        // Print spaces
        for (int space = 1; space <= n - i; space++) { // Print spaces for alignment
            printf("  ");
        }
        // Print characters
        for (int k = 1; k <=i; k++) {
            printf("%c ", ch + (k - 1)); // Print the increasing part of the pyramid
        }
        for (int k = i - 1; k >= 1; k--) {
            printf("%c ", ch + (k - 1)); // reverse part of the pyramid
        }
        printf("\n");
    }
}
int main() {
    int n;
    
    printf("Enter the number of rows for the character pyramid: ");
    scanf("%d", &n);
    
    printCharacterPyramid(n);
    
    return 0;
}
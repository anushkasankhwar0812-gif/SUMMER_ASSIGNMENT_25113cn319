//write a program to print number pyramid.
#include <stdio.h>
void printNumberPyramid(int n) {
    for (int i = 1; i <= n; i++) {
        // Print spaces
        for (int space = 1; space <= n - i; space++) {
            printf("  ");
        }
        // Print numbers
        for (int k = 1; k <= i; k++) {
            printf("%d ", k); // Print the increasing part of the pyramid
        }
        for (int k = i - 1; k >= 1; k--) {
            printf("%d ", k); // reverse part of the pyramid
        }
        printf("\n");
    }
}
int main() {
    int n;
    printf("Enter the number of rows for the number pyramid: ");
    scanf("%d", &n);
    
    printNumberPyramid(n);
    
    return 0;
}


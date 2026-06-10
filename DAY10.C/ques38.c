//write a program to print  reverse star pyramid.
#include <stdio.h>
void printReverseStarPyramid(int n) {
    for (int i = n; i >= 1; i--) {
        // Print spaces
        for (int space = 1; space <= n - i; space++) {
            printf("  ");
        }
        // Print stars
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("* ");
        }
        printf("\n");
    }
}
int main() {
    int n;
    
    printf("Enter the number of rows for the reverse star pyramid: ");
    scanf("%d", &n);
    
    printReverseStarPyramid(n);
    
    return 0;
}

//write a program to print star pyramids .
#include <stdio.h>
void printStarPyramid(int n) {
    for (int i = 1; i <= n; i++) {
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
    
    printf("Enter the number of rows for the star pyramid: ");
    scanf("%d", &n);
    
    printStarPyramid(n);
    
    return 0;
}
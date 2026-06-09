//write a program to print hollow square pattern.
#include <stdio.h>
void printHollowSquarePattern(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == 1 || i == n || j == 1 || j == n) {
                printf("* "); // Print star for the borders
            } else {
                printf("  "); // Print space for the hollow part
            }
        }
        printf("\n");
    }
}
int main() {
    int n;
    
    printf("Enter the size of the hollow square pattern: ");
    scanf("%d", &n);
    
    printHollowSquarePattern(n);
    
    return 0;
}
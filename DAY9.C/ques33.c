//write a program to print reverse  star pattern.
#include <stdio.h>
void printReverseStarPattern(int n) {
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}
int main() {
    int n;
    
    printf("Enter the number of rows for the reverse star pattern: ");
    scanf("%d", &n);
    
    printReverseStarPattern(n);
    
    return 0;
}
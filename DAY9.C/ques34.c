//write a program to print reverse number triangle
#include <stdio.h>
void printReverseNumberTriangle(int n) {
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
}
int main() {
    int n;
    
    printf("Enter the number of rows for the reverse number triangle: ");
    scanf("%d", &n);
    
    printReverseNumberTriangle(n);
    
    return 0;
}
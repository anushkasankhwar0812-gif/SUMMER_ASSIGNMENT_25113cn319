//write a program to print repeated character pattern.
#include <stdio.h>
void printRepeatedCharacterPattern(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%c ", 'A' + i - 1); // Print the character corresponding to the current row
        }
        printf("\n");
    }
}
int main() {
    int n;
    
    printf("Enter the number of rows for the repeated character pattern: ");
    scanf("%d", &n);
    
    printRepeatedCharacterPattern(n);
    
    return 0;
}

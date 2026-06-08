//write a program to print repeated  number pattern.
#include <stdio.h>
int main() {
    
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", i); // Print the current row number
        }
        printf("\n");
    }
    
    return 0;
}
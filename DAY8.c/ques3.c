//write a program to print character triangle.
#include <stdio.h>
int main() {
    
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%c ", 'A' + j - 1); // Print characters starting from 'A'
        }
        printf("\n");
    }
    
    return 0;
}
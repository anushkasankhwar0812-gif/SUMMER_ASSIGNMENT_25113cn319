//write a program to write function to find sum of two numbers.
#include <stdio.h>
int sum(int a, int b) {
    return a + b; // Return the sum of a and b
}

int main() {
    int x = 5, y = 10;
    printf("Sum of %d and %d is %d\n", x, y, sum(x, y));
    return 0;
}


// Write a program to find the factorial of a number using recursion.
#include <stdio.h>
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
int main() {
    int n;
    printf("Enter a number to find its factorial: ");
    scanf("%d", &n);
    if (n < 0) {
        printf("Factorial is not defined for negative numbers.");
    } else {
        printf("The factorial of %d is %d", n, factorial(n));
    }
    return 0;
}

//write program to recursve fibonacci.
#include <stdio.h>
int fibonacci(int n) {
    if (n == 0) {
        return 0; // Base case: Fibonacci of 0 is 0
    } else if (n == 1) {
        return 1; // Base case: Fibonacci of 1 is 1
    }
    return fibonacci(n - 1) + fibonacci(n - 2); // Recursive case
}
int main() {
    int n;
    
    printf("Enter a number to find its Fibonacci: ");
    scanf("%d", &n);
    
    if (n < 0) {
        printf("Fibonacci is not defined for negative numbers.\n");
    } else {
        int result = fibonacci(n);
        printf("Fibonacci of %d is: %d\n", n, result);
    }
    
    return 0;
}

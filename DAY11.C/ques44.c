//write a program to write function to find factorial.
#include <stdio.h>
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1; // Factorial of 0 and 1 is 1
    }
    return n * factorial(n - 1); // Recursive call to calculate factorial
}

int main() {
    int number;
    
    printf("Enter a number to find its factorial: ");
    scanf("%d", &number);
    
    printf("Factorial of %d is %d\n", number, factorial(number));
    
    return 0;
}

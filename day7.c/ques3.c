//write program to recursive sum of digrits.
#include <stdio.h>
int sumOfDigits(int n) {
    if (n == 0) {
        return 0; // Base case: sum of digits of 0 is 0
    }
    return (n % 10) + sumOfDigits(n / 10); // Recursive case
}
int main() {
    int n;
    
    printf("Enter a number to find the sum of its digits: ");
    scanf("%d", &n);
    
    if (n < 0) {
        printf("Sum of digits is not defined for negative numbers.\n");
    } else {
        int result = sumOfDigits(n);
        printf("Sum of digits of %d is: %d\n", n, result);
    }
    
    return 0;
}

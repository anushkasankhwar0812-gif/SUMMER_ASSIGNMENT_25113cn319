//write a program to recursive reverse number.
#include <stdio.h>
#include <math.h>
int reverseNumber(int n) {
    if (n < 10) {
        return n; // Base case: single digit number is its own reverse
    }
    int lastDigit = n % 10; // Get the last digit
    int remainingNumber = n / 10; // Get the remaining number
    int reversedRemaining = reverseNumber(remainingNumber); // Recursive call on the remaining number
    return lastDigit * pow(10, (int)log10(remainingNumber) + 1) + reversedRemaining; // Combine last digit with reversed remaining
}
int main() {
    int n;
    
    printf("Enter a number to reverse: ");
    scanf("%d", &n);
    
    if (n < 0) {
        printf("Reverse is not defined for negative numbers.\n");
    } else {
        int result = reverseNumber(n);
        printf("Reverse of %d is: %d\n", n, result);
    }
    
    return 0;
}

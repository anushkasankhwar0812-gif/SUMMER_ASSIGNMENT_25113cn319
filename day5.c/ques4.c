//write a program to find largest prime factor
#include <stdio.h>
int main() {
    int n, largest = -1;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    // Check for number of 2s that divide n
    while (n % 2 == 0) {
        largest = 2;
        n /= 2;
    }
    
    // n must be odd at this point, so we can skip even numbers
    for (int i = 3; i <= n / 2; i += 2) {
        while (n % i == 0) {
            largest = i;
            n /= i;
        }
    }
    
    // This condition is to check if n is a prime number greater than 2
    if (n > 2) {
        largest = n;
    }
    
    if (largest != -1) {
        printf("The largest prime factor is: %d\n", largest);
    } else {
        printf("No prime factors found.\n");
    }
    
    return 0;
}

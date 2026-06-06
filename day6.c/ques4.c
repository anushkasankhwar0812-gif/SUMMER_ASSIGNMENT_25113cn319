//write program to find x raised to the power n without using 'pow' function
#include <stdio.h>
double power(double x, int n) {
    double result = 1.0;
    int absN = n < 0 ? -n : n; // Get absolute value of n
    
    for (int i = 0; i < absN; i++) {
        result *= x;
    }
    
    if (n < 0) {
        return 1.0 / result; // If n is negative, return the reciprocal
    }
    
    return result;
}
int main() {
    double x;
    int n;
    
    printf("Enter a base number (x): ");
    scanf("%lf", &x);
    
    printf("Enter an exponent (n): ");
    scanf("%d", &n);
    
    double result = power(x, n);
    printf("%.2lf raised to the power of %d is: %.2lf\n", x, n, result);
    
    return 0;
}
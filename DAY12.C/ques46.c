//write a program to write function for armstrong
#include <stdio.h>
#include <math.h>

int isArmstrong(int n) {
    int original = n;
    int sum = 0;
    int digit;
    while (n > 0) {
        digit = n % 10;
        sum += pow(digit, 3);
        n /= 10;
    }
    return sum == original;
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (isArmstrong(num)) {
        printf("The number is an Armstrong number.\n");
    } else {
        printf("The number is not an Armstrong number.\n");
    }
    return 0;
}

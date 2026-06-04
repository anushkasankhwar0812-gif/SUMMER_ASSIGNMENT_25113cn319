//Write a program to Check Armstrong number.
#include <stdio.h>
#include <math.h>

int main() {
    int num, temp, rem, digits = 0;
    double sum = 0;

    printf("Enter number: ");
    scanf("%d", &num);

    temp = num;

    while (temp != 0) {
        temp /= 10;
        digits++;
    }

    temp = num;

    while (temp != 0) {
        rem = temp % 10;
        sum += pow(rem, digits);
        temp /= 10;
    }

    if ((int)sum == num)
        printf("Armstrong Number");
    else
        printf("Not Armstrong Number");

    return 0;
}

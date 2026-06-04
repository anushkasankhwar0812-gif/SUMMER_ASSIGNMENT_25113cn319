//Write a program to Print Armstrong numbers in a range.
#include <stdio.h>
#include <math.h>

int isArmstrong(int num) {
    int temp = num, rem, digits = 0;
    double sum = 0;

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

    return (int)sum == num;
}

int main() {
    int start, end;

    printf("Enter range (start end): ");
    scanf("%d %d", &start, &end);

    printf("Armstrong numbers in range: ");

    for (int i = start; i <= end; i++) {
        if (isArmstrong(i)) {
            printf("%d ", i);
        }
    }

    return 0;
}

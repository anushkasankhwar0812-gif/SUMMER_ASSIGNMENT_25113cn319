<<<<<<< HEAD
// Write a program to count the number of digits in a given number.
=======
//Write a program to count the number of digits in a given number.
>>>>>>> 064c965d1ab0da584299faa299015c63b842135b
#include <stdio.h>

int main() {
    int num, count = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num == 0) {
        count = 1;
    } 
    else {
        if (num < 0) {
            num = -num; // handle negative numbers
        }

        while (num != 0) {
            num /= 10;
            count++;
        }
    }

    printf("Number of digits = %d\n", count);

    return 0;
}

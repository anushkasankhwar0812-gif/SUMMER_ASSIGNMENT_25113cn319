//write a program to find the sum of first n natural numbers
<<<<<<< HEAD
#include <stdio.h>  
=======
#include<stdio.h>  
>>>>>>> 064c965d1ab0da584299faa299015c63b842135b
int main() {
    int n, i, sum=0;
    printf("enter the n natural numbers:");
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        sum += i;
    }
    printf("the sum of first %d natural numbers is %d", n, sum);
    return 0;
}

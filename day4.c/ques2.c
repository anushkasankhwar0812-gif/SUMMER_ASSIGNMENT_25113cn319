//Write a program to Find nth Fibonacci term
#include <stdio.h>

int main() {
    int n, a = 0, b = 1, next;

    printf("Enter n: ");
    scanf("%d", &n);

    if (n == 1) {
        printf("%d", a);
        return 0;
    }

    for (int i = 2; i < n; i++) {
        next = a + b;
        a = b;
        b = next;
    }

    printf("%d", b);

    return 0;
}

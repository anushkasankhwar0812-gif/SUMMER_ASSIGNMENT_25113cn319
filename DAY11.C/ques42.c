//write a program to write function  to find maximum.
#include <stdio.h>
int findMaximum(int a, int b) {
    if (a > b) {
        return a; // Return a if it is greater than b
    } else {
        return b; // Return b if it is greater than or equal to a
    }
}

int main() {
    int x = 5, y = 10;
    printf("Maximum of %d and %d is %d\n", x, y, findMaximum(x, y));
    return 0;
}

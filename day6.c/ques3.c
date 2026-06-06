//write a program to count set bits in a number
#include <stdio.h>
int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        count += n & 1; // Increment count if the last bit is 1
        n >>= 1; // Right shift n by 1 to check the next bit
    }
    return count;
}
int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    int setBits = countSetBits(n);
    printf("Number of set bits in %d is: %d\n", n, setBits);
    
    return 0;
}

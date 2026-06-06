//write a program to  convert binary to decimal
#include <stdio.h>
#include <math.h>
int main() {
    char binary[32];
    int decimal = 0, length;
    
    printf("Enter a binary number: ");
    scanf("%s", binary);
    
    // Calculate the length of the binary string
    for (length = 0; binary[length] != '\0'; length++);
    
    // Convert binary to decimal
    for (int i = 0; i < length; i++) {
        if (binary[length - 1 - i] == '1') {
            decimal += pow(2, i);
        }
    }
    
    printf("Decimal representation: %d\n", decimal);
    
    return 0;
}
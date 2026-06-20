//write a program to find row wise sum of a matrix.
#include <stdio.h>
int main() {
    int rows, cols;
    printf("Enter the number of rows and columns: ");
    scanf("%d %d", &rows, &cols);

    int matrix[rows][cols], rowSum[rows];

    printf("Enter elements of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Calculating row-wise sum
    for (int i = 0; i < rows; i++) {
        rowSum[i] = 0; // Initialize row sum to zero
        for (int j = 0; j < cols; j++) {
            rowSum[i] += matrix[i][j];
        }
    }

    // Displaying the row-wise sums
    printf("Row-wise sums of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        printf("Sum of row %d: %d\n", i + 1, rowSum[i]);
    }

    return 0;
}

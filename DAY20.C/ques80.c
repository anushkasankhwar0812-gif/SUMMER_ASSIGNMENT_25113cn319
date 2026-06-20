//write a program to find column wise sum of a matrix.
#include <stdio.h>
int main() {
    int rows, cols;
    printf("Enter the number of rows and columns: ");
    scanf("%d %d", &rows, &cols);

    int matrix[rows][cols], colSum[cols];

    printf("Enter elements of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Calculating column-wise sum
    for (int j = 0; j < cols; j++) {
        colSum[j] = 0; // Initialize column sum to zero
        for (int i = 0; i < rows; i++) {
            colSum[j] += matrix[i][j];
        }
    }

    // Displaying the column-wise sums
    printf("Column-wise sums of the matrix:\n");
    for (int j = 0; j < cols; j++) {
        printf("Sum of column %d: %d\n", j + 1, colSum[j]);
    }

    return 0;
}

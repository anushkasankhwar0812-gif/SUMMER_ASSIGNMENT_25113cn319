//write a program to find 'pair with given sum in array.
#include <stdio.h>
void findPairsWithSum(int arr[], int n, int targetSum) {
    printf("Pairs with sum %d are:\n", targetSum);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == targetSum) {
                printf("(%d, %d)\n", arr[i], arr[j]);
            }
        }
    }
}
int main() {
    int arr[100], n, targetSum;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the target sum: ");
    scanf("%d", &targetSum);

    findPairsWithSum(arr, n, targetSum);

    return 0;
}
//write a program  to merge arrays.
#include <stdio.h>
void mergeArrays(int arr1[], int n1, int arr2[], int n2, int merged[]) {
    for (int i = 0; i < n1; i++) {
        merged[i] = arr1[i];
    }
    for (int j = 0; j < n2; j++) {
        merged[n1 + j] = arr2[j];
    }
}
int main() {
    int arr1[100], arr2[100], merged[200];
    int n1, n2;

    printf("Enter the number of elements in the first array: ");
    scanf("%d", &n1);

    printf("Enter %d elements for the first array:\n", n1);
    for (int i = 0; i < n1; i++) {
        scanf("%d", &arr1[i]);
    }

    printf("Enter the number of elements in the second array: ");
    scanf("%d", &n2);

    printf("Enter %d elements for the second array:\n", n2);
    for (int j = 0; j < n2; j++) {
        scanf("%d", &arr2[j]);
    }

    mergeArrays(arr1, n1, arr2, n2, merged);

    printf("Merged array is: ");
    for (int k = 0; k < n1 + n2; k++) {
        printf("%d ", merged[k]);
    }
    printf("\n");

    return 0;
}

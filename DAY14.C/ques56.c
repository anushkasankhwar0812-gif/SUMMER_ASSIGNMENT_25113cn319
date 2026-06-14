//write a program find duplicates in array
#include <stdio.h>
void findDuplicates(int arr[], int n) {
    printf("Duplicate elements in the array are: ");
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                printf("%d ", arr[i]);
                break; // Break to avoid printing the same duplicate multiple times
            }
        }
    }
}
int main() {
    int arr[100], n;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    findDuplicates(arr, n);

    return 0;
}

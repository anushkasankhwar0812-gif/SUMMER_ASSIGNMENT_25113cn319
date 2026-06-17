//write a program to find common elements.
#include <stdio.h>
void findCommonElements(int arr1[], int n1, int arr2[], int n2) {
    printf("Common elements are: ");
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n2; j++) {
            if (arr1[i] == arr2[j]) {
                printf("%d ", arr1[i]);
                break; // Break to avoid printing the same element multiple times
            }
        }
    }
}
int main() {
    int arr1[100], arr2[100];
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

    findCommonElements(arr1, n1, arr2, n2);

    return 0;
} 


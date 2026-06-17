//write a program to intersection of arrays.
#include <stdio.h>
int findIntersection(int arr1[], int n1, int arr2[], int n2, int intersection[]) {
    int k = 0;
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n2; j++) {
            if (arr1[i] == arr2[j]) {
                intersection[k++] = arr1[i];
                break; // Break to avoid adding the same element multiple times
            }
        }
    }
    return k; // Return the size of the intersection array
}
int main() {
    int arr1[100], arr2[100], intersection[100];
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

    int intersectionSize = findIntersection(arr1, n1, arr2, n2, intersection);

    printf("Intersection of the arrays is: ");
    for (int k = 0; k < intersectionSize; k++) {
        printf("%d ", intersection[k]);
    }
    printf("\n");

    return 0;
}
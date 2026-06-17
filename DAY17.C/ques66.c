//write a program to union of arrays.
#include <stdio.h>

int findUnion(int arr1[], int n1, int arr2[], int n2, int unionArr[]) {
    int i = 0, j = 0, k = 0;

    while (i < n1 && j < n2) {
        if (arr1[i] < arr2[j]) {
            unionArr[k++] = arr1[i++];
        } else if (arr2[j] < arr1[i]) {
            unionArr[k++] = arr2[j++];
        } else {
            unionArr[k++] = arr1[i++];
            j++;
        }
    }

    while (i < n1) {
        unionArr[k++] = arr1[i++];
    }

    while (j < n2) {
        unionArr[k++] = arr2[j++];
    }

    return k;
}

int main() {
    int arr1[100], arr2[100], unionArr[200];
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

    int unionSize = findUnion(arr1, n1, arr2, n2, unionArr);

    printf("Union of the arrays is: ");
    for (int k = 0; k < unionSize; k++) {
        printf("%d ", unionArr[k]);
    }
    printf("\n");

    return 0;
}

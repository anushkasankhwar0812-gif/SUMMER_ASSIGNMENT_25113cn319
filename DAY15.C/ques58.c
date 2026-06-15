//write a program to rotate array left.
#include <stdio.h>
void rotateLeft(int arr[], int n, int d) {
    printf("Array after left rotation: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[(i + d) % n]);
    }
}
int main() {
    int arr[100], n, d;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the number of positions to rotate left: ");
    scanf("%d", &d);

    rotateLeft(arr, n, d);

    return 0;
}

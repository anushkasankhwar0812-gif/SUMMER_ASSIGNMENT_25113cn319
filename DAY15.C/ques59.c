//write a program to rotate array right.
#include <stdio.h>
void rotateRight(int arr[], int n, int d) {
    printf("Array after right rotation: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[(i - d + n) % n]);
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

    printf("Enter the number of positions to rotate right: ");
    scanf("%d", &d);

    rotateRight(arr, n, d);

    return 0;
}

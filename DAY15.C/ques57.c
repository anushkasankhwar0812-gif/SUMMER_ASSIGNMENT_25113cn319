//write a program to reverse an array.
 #include <stdio.h>
void reverseArray(int arr[], int n) {
    printf("Reversed array is: ");
    for (int i = n - 1; i >= 0; i--) {
        printf("%d ", arr[i]);
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

    reverseArray(arr, n);

    return 0;
}

//write a program to frequency of an element 
#include <stdio.h>
int frequency(int arr[], int n, int key) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            count++;
        }
    }
    return count;
}
int main() {
    int arr[100], n, key;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the element to find its frequency: ");
    scanf("%d", &key);

    int freq = frequency(arr, n, key);
    printf("Frequency of %d in the array is: %d\n", key, freq);

    return 0;
}

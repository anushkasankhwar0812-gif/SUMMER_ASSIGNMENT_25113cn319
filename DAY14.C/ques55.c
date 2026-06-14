//write a program to find second largest element 
#include <stdio.h>
int secondLargest(int arr[], int n) {
    if (n < 2) {
        return -1; // Not enough elements to find the second largest
    }

    int largest = arr[0];
    int secondLargest = -1;

    for (int i = 1; i < n; i++) {
        if (arr[i] > largest) {
            secondLargest = largest;
            largest = arr[i];
        } else if (arr[i] > secondLargest && arr[i] != largest) {
            secondLargest = arr[i];
        }
    }

    return secondLargest;
}
int main() {
    int arr[100], n;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int result = secondLargest(arr, n);
    if (result != -1) {
        printf("The second largest element is: %d\n", result);
    } else {
        printf("There is no second largest element.\n");
    }

    return 0;
}

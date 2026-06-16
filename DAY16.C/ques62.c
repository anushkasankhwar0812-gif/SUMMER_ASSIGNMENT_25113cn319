//write a program to find maximum frequency element.
#include <stdio.h>
int findMaxFrequency(int arr[], int n) {
    int maxCount = 0;
    int maxElement = arr[0];

    for (int i = 0; i < n; i++) {
        int count = 1; // Count the current element
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }
        if (count > maxCount) {
            maxCount = count;
            maxElement = arr[i];
        }
    }
    return maxElement; // Return the element with maximum frequency
}
int main() {
    int arr[100], n;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int maxFreqElement = findMaxFrequency(arr, n);
    printf("The element with maximum frequency is: %d\n", maxFreqElement);

    return 0;
}

#include <stdio.h>

// Function to find the maximum and minimum elements in an array
void findMinMax(int arr[], int low, int high, int *max, int *min) {
    int mid, max1, min1, max2, min2;

    // Base case: If the array has only one element
    if (low == high) {
        *max = *min = arr[low];
        return;
    }

    // If the array has two elements
    if (high == low + 1) {
        if (arr[low] > arr[high]) {
            *max = arr[low];
            *min = arr[high];
        } else {
            *max = arr[high];
            *min = arr[low];
        }
        return;
    }

    // If the array has more than two elements, divide it into two halves
    mid = (low + high) / 2;
    findMinMax(arr, low, mid, &max1, &min1);
    findMinMax(arr, mid + 1, high, &max2, &min2);

    // Combine the results of the two halves
    if (max1 > max2)
        *max = max1;
    else
        *max = max2;

    if (min1 < min2)
        *min = min1;
    else
        *min = min2;
}

int main() {
    int n;

    // Input the size of the array
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int arr[n];

    // Input array elements
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    int max, min;

    // Find the maximum and minimum elements in the array
    findMinMax(arr, 0, n - 1, &max, &min);

    // Display the results
    printf("Maximum element: %d\n", max);
    printf("Minimum element: %d\n", min);

    return 0;
}


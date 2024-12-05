#include <stdio.h>

int binary_search(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;  // Calculate the middle index

        if (arr[mid] == key) {
            return mid;  // Element found
        } else if (arr[mid] < key) {
            low = mid + 1;  // Search in the right half
        } else {
            high = mid - 1;  // Search in the left half
        }
    }

    return -1;  // Element not found
}

int main() {
    int A[] = {3, 10, 15, 20, 35, 40, 60};
    int n = sizeof(A) / sizeof(A[0]);  // Get the size of the array
    int key = 15;  // Element to search

    int found_index = binary_search(A, 0, n - 1, key);

    if (found_index != -1) {
        printf("Element %d found at index %d\n", key, found_index);
    } else {
        printf("Element %d not found in the array\n", key);
    }

    return 0;
}

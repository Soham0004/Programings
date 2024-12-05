#include <stdio.h>

int max_min_dc(int A[], int i, int j) {
  if (i == j) {
    return A[i]; // Both max and min are the same element
  } else if (i == j - 1) {
    return (A[i] > A[j]) ? A[i] : A[j]; // Compare two elements
  } else {
    int mid = (i + j) / 2;
    // Recursively find max and min in left and right halves
    int max1 = max_min_dc(A, i, mid);
    int min1 = max_min_dc(A, i, mid);
    int max2 = max_min_dc(A, mid + 1, j);
    int min2 = max_min_dc(A, mid + 1, j);
    // Update max and min based on both halves
    int max_element = (max1 > max2) ? max1 : max2;
    int min_element = (min1 < min2) ? min1 : min2;
    return max_element | min_element; // Return both max and min in one integer
  }
}

int main() {
  int A[] = {5, 3, 1, 7, 2, 8}; // Sample array
  int max_min = max_min_dc(A, 0, 5); // Find max and min in the whole array

  // Extract and print the max and min values
  int max_value = max_min >> 16;
  int min_value = max_min & 0xFFFF;

  printf("Maximum element: %d\n", max_value);
  printf("Minimum element: %d\n", min_value);

  return 0;
}

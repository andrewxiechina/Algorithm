# Count Sort

```cpp
#include <iostream>
using namespace std;
#define RANGE 100

// A utility function to print an array
void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
}

int* sort(int a[], int n) {
  // Count
  int c[RANGE] = {0};
  for(int i = 0; i < n; i++){
    c[a[i]]++;
  }
  
  // Accumulate so that count now contains position
  for(int i = 1; i < RANGE; i++){
    c[i] += c[i-1];
  }
  
  
  // Build output array
  int *output = new int[n];
  for(int i = 0; i < n; i++){
    output[c[a[i]] - 1] = a[i];
    c[a[i]]--;
  }
  
  return output;
}

int main() {
  int n = 8;
  int a[] = {63, 25, 73, 1, 1, 2, 2, 98};
  int *a_sorted = sort(a, n);
    
  print(a_sorted, n);
  
  return 0;
}

```
Problem:
https://www.hackerrank.com/challenges/countingsort2/problem
Reference:
https://www.geeksforgeeks.org/radix-sort/

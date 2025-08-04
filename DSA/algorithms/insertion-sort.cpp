#include <iostream>
#include <vector>

void insertionSort(std::vector<int> &arr) {
  int size = arr.size();

  for (int i = 1; i < size; i++) {
    int key = arr[i];

    int j = i - 1;

    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}
void printArray(const std::vector<int> &arr) {
  for (int num : arr)
    std::cout << num << " ";
  std::cout << "\n";
}

int main() {
  std::vector<int> numeros = {9, 3, 1, 5, 4};

  std::cout << "Antes da ordenação:\n";
  printArray(numeros);

  insertionSort(numeros);

  std::cout << "Depois da ordenação:\n";
  printArray(numeros);

  return 0;
}
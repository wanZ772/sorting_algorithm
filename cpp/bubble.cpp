#include <iostream>

using namespace std;

int main()  {
    int unsorted[10] = {7, 2, 9, 5, 1, 8, 3, 10, 6, 4};
    int length = sizeof(unsorted) / sizeof(unsorted[0]);
    for (int i = 0; i < length; i++)    {
        for (int j = 0; j < length - 1; j++)    {
            if (unsorted[j] > unsorted[j+1])    {
                int temp = unsorted[j];
                unsorted[j] = unsorted[j+1];
                unsorted[j+1] = temp;
            }
        }
    }
    cout << "Sorted array: ";
    for (int i = 0; i < length; i++)    {
        cout << " " << unsorted[i];
    }
    return 0;
}
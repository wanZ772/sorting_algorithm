#include <iostream>

using namespace std;

int main()  {
    int unsorted[10] = {7, 2, 9, 5, 1, 8, 3, 10, 6, 4};
    int length = sizeof(unsorted) / sizeof(unsorted[0]);
    for (int i = 0; i < length; i++)    {
        int selected = 1;
        for (int j = 0; j < length; j++)    {
            if (unsorted[selected] < unsorted[j])    {
                int temp = unsorted[selected];
                unsorted[selected] = unsorted[j];
                unsorted[j] = temp;
            }
            selected++;
        }
    }
    cout << "Sorted array: ";
    for (int i = 0; i < length; i++)    {
        cout << " " << unsorted[i];
    }
    return 0;
}
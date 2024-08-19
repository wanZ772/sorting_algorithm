#include <iostream>

using namespace std;
int unsorted[10] = {7, 2, 9, 5, 1, 8, 3, 10, 6, 4};
void merge(int array[], int size) {
    if (size >= 1)   {
        cout << "recursion: ";
        for (int i = 0; i < size; i++)    {
        cout << " " << unsorted[i];
    }
    cout << size / 2 << endl;
    merge(array, size-1);
    }   else    {
        cout << "recursion finished" << endl;
    }
}

int main()  {
    
    int length = sizeof(unsorted) / sizeof(unsorted[0]);
    merge(unsorted, length);
    // cout << "Sorted array: ";
    // for (int i = 0; i < length; i++)    {
    //     cout << " " << unsorted[i];
    // }
    return 0;
}
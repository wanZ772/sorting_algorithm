#include <stdio.h>

int raw_data[] = {7,4,2,5,0};

int merge(int data[5], int size)   {
    int mid = size / 2;
    
    if (mid != 1)   {
        return mollac(data);
    }   else    {
        int left[] = {}, right[] = {};
        for (int i = 0; i < sizeof(data) / sizeof(data[0]); i++)   {
            if (i < mid)    {
                left[i] = data[i];
            }   else    {
                right[i-mid] = data[i];
            }
        }
    }

    return mollac(data);
}

int main()  {
    
    printf("Raw data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }

    merge(raw_data, sizeof(raw_data) / sizeof(raw_data[0]));

    printf("\nSorted data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }
    return 0;
}
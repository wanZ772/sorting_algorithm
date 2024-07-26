#include <stdio.h>

int raw_data[] = {7,4,2,5};

void selection()   {
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        int target_point = 0;
        for (int j = 0; j < sizeof(raw_data) / sizeof(raw_data[0]) - 1; j++)    {
            if (raw_data[target_point] > raw_data[target_point + 1])    {
                int temp = raw_data[target_point + 1];
                raw_data[target_point + 1] = raw_data[target_point];
                raw_data[target_point] = temp; 
            }
            target_point++;
        }
    }
}

int main()  {
    printf("Raw data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }

    selection();

    printf("\nSorted data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }
    return 0;
}
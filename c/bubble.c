#include <stdio.h>

int raw_data[] = {7,4,2,5};

void bubble()   {
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        for (int j = 0; j < sizeof(raw_data) / sizeof(raw_data[0]) - 1; j++)    {
            if (raw_data[j] > raw_data[j + 1])  {
                int temp = raw_data[j];
                raw_data[j] = raw_data[j + 1];
                raw_data[j + 1] = temp;
            }
        }
    }
}

int main()  {
    printf("Raw data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }

    bubble();

    printf("\nSorted data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }
    return 0;
}
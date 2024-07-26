#include <stdio.h>

int raw_data[] = {7,4,2,5};

void insertion()   {
    for (int i = 1; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        int j = i;
        while (j > 0)   {
            if (raw_data[j] < raw_data[j-1])    {
                int temp = raw_data[j];
                raw_data[j] = raw_data[j-1];
                raw_data[j-1] = temp;
            }
            j--;
        }
    }
}

int main()  {
    printf("Raw data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }

    insertion();

    printf("\nSorted data: ");
    for (int i = 0; i < sizeof(raw_data) / sizeof(raw_data[0]); i++)    {
        printf("%d ", raw_data[i]);
    }
    return 0;
}
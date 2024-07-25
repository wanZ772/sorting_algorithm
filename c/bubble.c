#include <stdio.h>

int unsorted[5] = {1,67,5,25,4};
int sorted[10];

int main()  {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (unsorted[i] < unsorted[j])  {
                sorted[i] = unsorted[i];
            }
        }
        printf("\n");
    }
    for (int i = 0; i < 5; i++) {
        printf("%d,", sorted[i]);
    }
    return 0;
}
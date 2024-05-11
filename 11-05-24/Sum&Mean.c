#include <stdio.h>

int main() {
    double sum = 0;
    int count = 0;

    while (1) {
        int num;
        scanf("%d", &num);
        if (num == -1) {
            break;
        }
        sum += num;
        count++;
    }

    double mean = sum / count;

    printf("Sum of the given %d numbers is : %.0f\n", count, sum);
    printf("Mean of the given %d numbers is : %.2f\n", count, mean);

    return 0;
}

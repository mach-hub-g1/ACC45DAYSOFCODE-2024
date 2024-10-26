#include <stdio.h>

int main() {
    int T; // Number of test cases
    scanf("%d", &T);

    while (T--) {
        int N; // Number of spooky days
        scanf("%d", &N);

        // Calculate the number of Tuesdays
        int tuesdays = (N + 1) / 7;

        // Print the result for the current test case
        printf("%d\n", tuesdays);
    }

    return 0;
}

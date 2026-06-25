//write a program to sort names alphabetically
#include <stdio.h>
#include <string.h>

int main() {
    char names[10][50];
    int n;

    printf("Enter the number of names: ");
    scanf("%d", &n);
    getchar(); // To consume the newline character

    for (int i = 0; i < n; i++) {
        printf("Enter name %d: ", i + 1);
        fgets(names[i], sizeof(names[i]), stdin);
        names[i][strcspn(names[i], "\n")] = '\0'; // Remove newline character
    }

    // Sorting names alphabetically
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strcmp(names[i], names[j]) > 0) {
                char temp[50];
                strcpy(temp, names[i]);
                strcpy(names[i], names[j]);
                strcpy(names[j], temp);
            }
        }
    }

    printf("Names in alphabetical order:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", names[i]);
    }

    return 0;
}
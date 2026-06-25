//write a C program to  sort words by length
#include <stdio.h>
#include <string.h>

int main() {
    char words[10][50];
    int n;

    printf("Enter the number of words: ");
    scanf("%d", &n);
    getchar(); // To consume the newline character

    for (int i = 0; i < n; i++) {
        printf("Enter word %d: ", i + 1);
        fgets(words[i], sizeof(words[i]), stdin);
        words[i][strcspn(words[i], "\n")] = '\0'; // Remove newline character
    }

    // Sorting words by length
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strlen(words[i]) > strlen(words[j])) {
                char temp[50];
                strcpy(temp, words[i]);
                strcpy(words[i], words[j]);
                strcpy(words[j], temp);
            }
        }
    }

    printf("Words in order of increasing length:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", words[i]);
    }

    return 0;
}
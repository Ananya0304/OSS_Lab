#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_PARAGRAPH 1000
#define MAX_WORDS 100
#define MAX_WORD_LEN 50

void toLowerCase(char *str) {
    for (int i = 0; str[i]; i++)
        str[i] = tolower(str[i]);
}

void removePunctuation(char *word) {
    int i = 0, j = 0;
    while (word[i]) {
        if (isalpha(word[i]) || isdigit(word[i]))
            word[j++] = word[i];
        i++;
    }
    word[j] = '\0';
}

int main() {
    char paragraph[MAX_PARAGRAPH];
    char words[MAX_WORDS][MAX_WORD_LEN];
    int freq[MAX_WORDS] = {0};
    int wordCount = 0;

    printf("Enter a paragraph:\n");
    fgets(paragraph, MAX_PARAGRAPH, stdin);

    char *token = strtok(paragraph, " \n");
    while (token != NULL) {
        char cleanedWord[MAX_WORD_LEN];
        strncpy(cleanedWord, token, MAX_WORD_LEN);
        cleanedWord[MAX_WORD_LEN - 1] = '\0';

        removePunctuation(cleanedWord);
        toLowerCase(cleanedWord);

        if (strlen(cleanedWord) == 0) {
            token = strtok(NULL, " \n");
            continue;
        }

        int found = 0;
        for (int i = 0; i < wordCount; i++) {
            if (strcmp(words[i], cleanedWord) == 0) {
                freq[i]++;
                found = 1;
                break;
            }
        }

        if (!found && wordCount < MAX_WORDS) {
            strcpy(words[wordCount], cleanedWord);
            freq[wordCount] = 1;
            wordCount++;
        }

        token = strtok(NULL, " \n");
    }

    printf("\nWord Frequencies:\n");
    for (int i = 0; i < wordCount; i++) {
        printf("%s: %d\n", words[i], freq[i]);
    }

    return 0;
}

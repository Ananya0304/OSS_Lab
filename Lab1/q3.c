#include <stdio.h>
#include <string.h>
int main() {
   char str[100];
   printf("Enter string: ");
   fgets(str,sizeof(str),stdin);
   int len=strlen(str);
   printf("Reversed Sring: ");
   for(int i=len-1;i>=0;i--){
    printf("%c",str[i]);
   }
   printf("\n");
   return 0;

}
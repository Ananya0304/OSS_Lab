#include<stdio.h>
int main(){
int row,col;
printf("Enter row of matrix:");
scanf("%d",&row);
printf("Enter column of matrix:");
scanf("%d",&col);
    int mat[row][col],trp[col][row];
    printf("Enter elements:");
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            scanf("%d",&mat[i][j]);
        }
    }
     for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
           trp[j][i]=mat[i][j];
        }
    }
    printf("Transpose:");
    for(int i=0;i<col;i++){
        for(int j=0;j<row;j++){
            printf("%d ",trp[i][j]);
        }
        printf("\n");
    }


}
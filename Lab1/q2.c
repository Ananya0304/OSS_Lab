#include <stdio.h>
int main() {
    int n;
    printf("Enter size of array:");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int sum=0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    float avg=(float)sum/n;
    printf("\n");
    printf("Average is: %.2f",avg);
    printf("\n");
}

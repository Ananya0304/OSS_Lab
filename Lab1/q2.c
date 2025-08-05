<<<<<<< HEAD
#inclue <stdio.h>
using namespace std;
int main(){
    int n;
    printf("Enter size of array:");
    scanf("%d",n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",arr[i]);
    }
    int sum=0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    sum/=n;
    printf("\n");
    printf("Average is: %d",sum);
    
=======
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
>>>>>>> aba4d62bc2d54bcbb327a47dd26f3d93f5e320f6

}

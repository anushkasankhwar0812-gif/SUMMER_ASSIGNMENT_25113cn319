#include  <stdio.h>  
int main() {
    int n, i, sum=0;
    printf("enter the n natural numbers:");
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        sum += i;
    }
    printf("the sum of first %d natural numbers is %d", n, sum);
    return 0;
}

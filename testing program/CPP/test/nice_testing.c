#include <stdio.h>
#include <math.h>
int main(){
    double c = 0.0673 * 1.24*0.55;
    double a;
    scanf("%lf",&a);
    a = pow(0.55 * a * a * 4.4, 0.976);
    printf("%f\n",a*c);
    return 0;
}
//USING HOMER SERIES

#include <stdio.h>


double func(int x, int n){
    static double result = 1;
    if (n == 0){
        return result;
    }
    result = 1+(result * x/n);
    return func(x, n-1);

}
int main(){
    printf("%lf\n", func(1,10));
    return 0;
}
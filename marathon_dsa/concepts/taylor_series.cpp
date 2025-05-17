//Code that calcualtes taylor series
#include <stdio.h>

double func(int x, int y){
    static double p = 1 , f= 1;
    double result;

    if (y == 0){
        return 1;
    }
    result = func(x, y-1);
    p=p*x;
    f=f*y;
    return result +p/f;
}

int main(){
    printf("%lf\n", func(4,10));
    return 0;
}
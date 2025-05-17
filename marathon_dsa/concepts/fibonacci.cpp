//CODE THAT SOLVE FIBONACCI SEQUENCE USING MEMOISATION

#include <stdio.h>

int array[10];

int fib(int n){
    if (n <= 1){
        array[n] = n;
        return n;
    }
    else{
        if (array[n-2] == -1){
        array[n-2] = fib(n-2);
    }
        if (array[n-1] == -1){
            array[n-1] = fib(n-1);
        }
        return array[n-2] + array[n-1];
    }
    
}

int main(){
    for (int i = 0; i < 10; i++){
        array[i] = -1;
    }
    printf("%d\n", fib(6));
    return 0;
}
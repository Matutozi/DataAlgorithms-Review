#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n = 5;
    int *p;

    p = &n;

    cout << n << endl;
    cout << *p << endl;

    int A[5] = {1,2,3,4,5};
    int *b;
    b = A;

    for (int i=0; i<5; i++){
        cout << A[i] << endl;
    }

    return 0;
}
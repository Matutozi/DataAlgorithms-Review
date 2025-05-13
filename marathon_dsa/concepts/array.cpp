#include <iostream>

using namespace std;

int main()
{
    int B[5] = {2,3,4,5,6};
    int A[5];
    A[0] = 12;
    A[1] = 15;
    A[2] = 25;
    A[3] = 30;
    A[4] = 35;

    for (int i=0; i < 5; i++){
        cout << B[i] << endl;
    }
    
    for (int x:A){
        cout << x << endl;
    }
    cout << sizeof(A) << endl;
    cout << sizeof(B) << endl;
    cout << A[1] << endl;
    return 0;
}
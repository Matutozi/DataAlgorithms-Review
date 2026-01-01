#include <iostream>

using namespace std;

class Array{
    private:
        int *A;
        int size;
        int length;
    public:
        Array(){
            size=10;
            A = new int[10];
            length=0;
        }
        Array(int size){
            size=size;
            length=0;
            A = new int[size];

        }
        ~Array(){
            delete []A;
        }


        void Display();
        void Insert(int index, int x);
        int Delete(int index); //theyb take no parameter of the array
};



void Array::Display(){
    for (int i=0; i < length; i++){
        cout << A[i] << " "; 
    }
    cout << endl;
}

void Array::Insert(int index, int x){
    if (index >= 0 && index < length)
    {
        for (int i=length-1; i>index; i--){
            A[i+1]=A[i];
        }
        A[index] = x;
        length++;
    }
}

int main(void){
    Array arr[10];
    arr.Insert(0, 5);
    arr.Insert(1, 6);
    arr.Insert(2, 9);

    arr.Display();

    return 0;
}
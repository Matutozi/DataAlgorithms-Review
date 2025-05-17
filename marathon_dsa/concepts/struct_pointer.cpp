#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;
struct Rectangle{
    int length;
    int breadth;
};

void fun(struct Rectangle r)
{
    cout << "Length" << r.length << endl << "Breadth" << r.breadth;
}
int main(void)
{
    struct Rectangle r = {1,5};
    fun(r);

    printf("Length %d \n Breadth %d\n", r.length, r.breadth);
    return 0;
}

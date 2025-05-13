#include <iostream>

using namespace std;

struct Card
{
    int face;
    int shape;
    int color;
};

struct Rectangle{
    int length;
    int breadth;
};

int main(){
    struct Card deck[52];
    struct Rectangle r1 = {10,5};
    printf("%lu\n", sizeof(r1));
    cout << endl;
    return 0;
    //we can use this to declare all the cards in a deck of card
}
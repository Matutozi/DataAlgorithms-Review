#include "main.h"

//function to print the list
void printList()
{
    struct node *p = header;
    printf("\n[ ");

    while (p != NULL)
    {
        printf(" %d ", p->data);
        p = p ->next;
    }
    printf(" ]\n");
}

void insertatbegin(int data)
{
    struct node *newnode = malloc(sizeof(struct node));
    newnode ->data = data;
    newnode ->next = header;
    header = newnode;
}
int main(void)
{
    insertatbegin(12);
    insertatbegin(22);
    insertatbegin(30);
    insertatbegin(44);
    insertatbegin(50);
    printf("Linked List: ");
   
   //  to print the entire list
   printList();
   return (0);
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node{
    int data;
    struct node* next;
};

struct node *head = NULL;
void printlist(void)
{
    struct node *p = head;

    while (p != NULL)
    {
        printf("%d\n", p->data);
        p = p->next;
    }
    printf("\n");
}

void insertatBegin(int data)
{
    struct node *newnode = malloc(sizeof(struct node));

    newnode ->data = data;
    newnode ->next = head;
    head = newnode;

}

void insertAtEnd(int data)
{
    struct node *newnode = malloc(sizeof(struct node));
    struct node *current = head;
    newnode ->data = data;

    while (current->next != NULL)
    {
        current = current->next;
    }
    current->next = newnode;
}

int main(void)
{
    insertatBegin(12);
    insertAtEnd(22);
    insertAtEnd(30);
    insertAtEnd(44);
    insertAtEnd(50);
    printf("Linked List: ");
    
    printlist();
    return (0);
}
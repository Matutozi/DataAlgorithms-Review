#ifndef MAIN_H
#define MAIN_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct node{
    int data;
    struct node *next;
};

struct node *header = NULL;
//struct node *current = NULL;

void printList();
void insertatbegin(int data);

#endif
#ifndef __MAIN_H__
#define __MAIN_H__


#include <stdlib.h>
#include <stdio.h>

typedef struct list_s{
    int *str;
    unsigned int len;
    struct list_s *next;

}list_s;

#endif __MAIN_H__
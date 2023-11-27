#include "main.h"

void insertAtFront(list_s** head, int new_data)
{
    list_s* new_node = (list_s *) malloc(sizeof(list_s));

    new_node->data = new_data;
    printf("%p\n", head);
    printf("%p\n", *head);
    new_node->next = *head;
    *head = new_node;
}

void printList(list_s* node)
{
	while (node != NULL) {
		printf(" %d", node->data);
		node = node->next;
	}
	printf("\n");
}

int main()
{
    list_s *head = NULL;
	insertAtFront(&head, 1);
	insertAtFront(&head, 2);
	insertAtFront(&head, 3);
	insertAtFront(&head, 4);
	insertAtFront(&head, 5);
	insertAtFront(&head, 6);
    
    printf("After inserting nodes at their front: ");
	printList(head);

	return 0;
}

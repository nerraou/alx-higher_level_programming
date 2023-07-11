#include "lists.h"

/**
 * check_cycle - check if linked list has cycle
 * @list: linked list head
 * Return: 1: if list has cycle, 0: if not
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step;
	listint_t *two_step;

	if (list == NULL || list->next == NULL)
		return (0);
	one_step = list;
	two_step = list->next;
	while (1)
	{
		if (one_step == NULL || two_step == NULL)
			break;
		if (one_step == two_step)
			return (1);
		one_step = one_step->next;
		if (two_step != NULL && two_step->next != NULL)
			two_step = two_step->next->next;
		else
			two_step = NULL;
	}
	return (0);
}

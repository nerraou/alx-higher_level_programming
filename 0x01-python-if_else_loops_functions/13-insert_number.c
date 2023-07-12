#include "lists.h"

/**
 * insert_node - insert node into sorted list
 * @head: list head
 * @number: value to be inserted
 * Return: the created node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *elem;
	listint_t *it;
	listint_t *prev;

	if (head == NULL)
		return (NULL);
	elem = malloc(sizeof(listint_t));
	if (elem == NULL)
		return (NULL);
	elem->n = number;
	elem->next = NULL;
	if (*head == NULL)
		*head = elem;
	else
	{
		prev = NULL;
		it = *head;
		while (it != NULL)
		{
			if (it->n >= number)
			{
				if (prev == NULL)
				{
					elem->next = *head;
					*head = elem;
					return (elem);
				}
				else
				{
					prev->next = elem;
					elem->next = it;
					return (elem);
				}
			}
			prev = it;
			it = it->next;
		}
		prev->next = elem;
	}
	return (elem);
}

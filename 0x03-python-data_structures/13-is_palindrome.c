#include "lists.h"

/**
 * reverse_listint - reverse linked list
 * @head: linked list head
 * Return: new linked list head
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next;
	listint_t *prev;

	if (!head)
		return (NULL);
	prev = NULL;
	if (*head == NULL || (*head)->next == NULL)
		return (*head);
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (prev);
}

/**
 * get_size - get list size
 * @head: list head
 * Return: list size
 */
int get_size(listint_t *head)
{
	int size;

	size = 0;
	while (head)
	{
		size++;
		head = head->next;
	}
	return (size);
}

/**
 * is_lists_equals - check if two linked lists are equal
 * @list_a: linked list head
 * @list_b: linked list head
 * @size: linked list size
 * Return: 1: if equal, othwewise: 0
 */
int is_lists_equals(listint_t *list_a, listint_t *list_b, int size)
{
	int i;

	i = 0;
	while (i < size)
	{
		if (list_a->n != list_b->n)
			return (0);
		i++;
		list_a = list_a->next;
		list_b = list_b->next;
	}
	return (1);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: list head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int i;
	int size;
	int half_size;
	listint_t *half;

	if (head == NULL || *head == NULL)
		return (1);
	size = get_size(*head);
	half = *head;
	half_size = size / 2;
	for (i = 0; i < half_size; i++)
	{
		half = half->next;
	}
	if (size % 2 == 1)
		half = half->next;
	reverse_listint(&half);
	size = is_lists_equals(*head, half, half_size);
	reverse_listint(&half);
	return (size);
}

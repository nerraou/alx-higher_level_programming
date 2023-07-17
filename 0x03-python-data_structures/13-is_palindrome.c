#include "lists.h"

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
 * list_to_array - list to array
 * @head: list head
 * @p_size: size pointer
 * Return: array of list values
 */
int *list_to_array(listint_t *head, int *p_size)
{
	int size;
	int *array;

	size = get_size(head);
	*p_size = size;
	array = malloc(sizeof(int) * size);
	if (!array)
		return (NULL);
	for (int i = 0; i < size; i++)
	{
		array[i] = head->n;
		head = head->next;
	}
	return (array);
}

/**
 * is_palindrome - check if linked list is palindrome
 * @head: list head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int size;
	int *array;
	int start;
	int end;

	if (!head)
		return (1);
	array = list_to_array(*head, &size);
	if (!array)
		return (0);
	start = 0;
	end = size - 1;
	while (start < end)
	{
		if (array[start] != array[end])
		{
			free(array);
			return (0);
		}
		start++;
		end--;
	}
	free(array);
	return (1);
}

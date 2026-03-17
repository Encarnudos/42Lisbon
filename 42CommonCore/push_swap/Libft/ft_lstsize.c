/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 19:46:28 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 15:35:15 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	count;

	count = 0;
	if (!lst)
		return (0);
	while (lst)
	{
		count++;
		lst = lst->next;
	}
	return (count);
}
/*
int	main(void)
{
	int	n1 = 1;
	t_list	*node1 = ft_lstnew(&n1);
	int	n2 = 1;
	t_list	*node2 = ft_lstnew(&n2);
	int	n3 = 1;
	t_list	*node3 = ft_lstnew(&n3);

	node1->next = node2;
	node2->next = node3;
	int	size = ft_lstsize(node1);
	printf("&d", size);
	free (node1);
	free (node2);
	free (node3);
	return (0);
}
*/

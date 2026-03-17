/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 19:57:41 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 15:39:14 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*node;

	if (!lst || !new)
		return ;
	if (!*lst)
	{
		*lst = new;
		return ;
	}
	node = *lst;
	while (node->next)
	{
		node = node->next;
	}
	node->next = new;
}
/*
int	main(void)
{
	int	n1 = 42;
	t_list	*node1 = ft_lstnew(&n1);
	int	n2 = 2;
	t_list	*node2 = ft_lstnew(&n2);

	ft_lstadd_back(&node1, node2);
	printf ("%d", *(int *)node1->content);
	printf ("%d", *(int *)node1->next->content);
	free (node1);
	free (node2);
	return (0);
}
*/

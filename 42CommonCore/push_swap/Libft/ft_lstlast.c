/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 19:52:11 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 16:29:43 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next)
	{
		lst = lst->next;
	}
	return (lst);
}
/*
int	main(void)
{
	int	n1 = 44;
	t_list	*node1 = ft_lstnew(&n1);
	int	n2 = 81;
	t_list	*node2 = ft_lstnew(&n2);
	int	n3 = 36;
	t_list	*node3 = ft_lstnew(&n3);

	node1->next = node2;
	node2->next = node3;
	t_list	*last_node = ft_lstlast(node1);
	printf("%d", *(int *)last_node->content);
	free (node3);
	free (node2);
	free (node1);
	return (0);
}
*/

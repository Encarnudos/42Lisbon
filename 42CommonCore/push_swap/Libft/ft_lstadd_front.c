/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 19:20:48 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 15:42:41 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!new || !lst)
		return ;
	new->next = *lst;
	*lst = new;
}
/*
int	main(void)
{
	int	n = 44;
	t_list	*node = ft_lstnew(&n);
	int	n1 = 81;
	t_list	*node1 = ft_lstnew(&n1);

	ft_lstadd_front(&node, node1);
	printf("%d", *(int *)node->content);
	printf("%d", *(int *)node->next->content);
	free(node);
	free(node1);
	return (0);
}
*/

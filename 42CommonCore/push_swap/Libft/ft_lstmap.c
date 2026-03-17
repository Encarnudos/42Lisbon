/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 22:12:23 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 17:41:07 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_node;
	t_list	*new_list;

	if (!lst || !f || !del)
		return (NULL);
	new_list = NULL;
	new_node = NULL;
	while (lst)
	{
		new_node = ft_lstnew(f(lst->content));
		if (!new_node)
		{
			ft_lstclear(&new_list, del);
			return (NULL);
		}
		ft_lstadd_back(&new_list, new_node);
		lst = lst->next;
	}
	return (new_list);
}
/*
void	*ft_f(void *content)
{
	int	*n = malloc(sizeof(int));
	*n = *(int *)content + 1;
	return n;
}

void	del_int(void *content)
{
	free(content);
}

int	main(void)
{
	int	x = 5;
	t_list	*lst = ft_lstnew(&x);
	t_list	*new = ft_lstmap(lst, ft_f, del_int);
	printf("%d", *(int *)new->content);
}
*/

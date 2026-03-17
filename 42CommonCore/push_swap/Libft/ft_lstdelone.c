/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 18:43:28 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 16:18:48 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void*))
{
	if (!lst || !del)
		return ;
	del(lst->content);
	free(lst);
}
/*
int	main(void)
{
	char	*str1 = ft_strdup("Hello");
	char	*str2 = ft_strdup("Snoop");
	t_list	*node1 = ft_lstnew(str1);
	t_list	*node2 = ft_lstnew(str2);
	node1->next = node2;
	printf("%d", ft_lstsize(node1));
	node1->next = NULL;
	ft_lstdelone(node2, free);
	printf("%d", ft_lstsize(node1));
	return (0);
}
*/

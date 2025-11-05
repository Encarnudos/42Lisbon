/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 22:12:23 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/05 22:12:37 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "libft.h"

t_list  *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
        void *new_content;
        t_list  *new_node;
        t_list  *new_list;

        if (!lst || !f || !del)
                return (NULL);
        new_list = NULL;
        while (lst)
        {
                new_content = f(lst->content);
                new_node = ft_lstnew(new_content);
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

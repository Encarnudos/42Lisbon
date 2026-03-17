/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 12:19:17 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/03 15:59:42 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	a;
	size_t	i;

	a = 0;
	i = 0;
	if (little[i] == 0)
		return ((char *)big);
	while (a < len && big[a])
	{
		i = 0;
		while (big[a + i] == little[i] && (a + i) < len)
		{
			if (little[i + 1] == '\0')
				return ((char *)(big + a));
			i++;
		}
		a++;
	}
	return (NULL);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 16:56:32 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 18:20:10 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*tmp;
	size_t			a;

	tmp = (unsigned char *)s;
	a = 0;
	while (a < n)
	{
		tmp[a] = (unsigned char)c;
		a++;
	}
	return (s);
}
/*
int	main(void)
{
	char	str[10];

	ft_memset(str, 'a', 5);
	printf("%s", str);
	return (0);
}
*/

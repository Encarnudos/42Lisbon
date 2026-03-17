/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 18:13:27 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 18:18:57 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dst, const void *src, size_t n)
{
	unsigned char	*tmp_dst;
	unsigned char	*tmp_src;
	size_t			count;

	count = 0;
	if (dst == (void *)0 && src == (void *)0)
		return (dst);
	tmp_dst = (unsigned char *)dst;
	tmp_src = (unsigned char *)src;
	if (tmp_dst > tmp_src)
	{
		while (n-- > 0)
		{
			tmp_dst[n] = tmp_src[n];
		}
	}
	else
	{
		while (count < n)
		{
			tmp_dst[count] = tmp_src[count];
			count++;
		}
	}
	return (dst);
}
/*
int	main(void)
{
	unsigned char	d[20] = "Snoop Miguel";
	const unsigned char	s[] = "Hello Snoop";

	ft_memmove(d, s, 5);
	d[10] = '\0';
	printf("%s", d);
	ft_memmove(d, s, 8);
	d[10] = '\0';
	printf("%s", d);
	return (0);
}
*/

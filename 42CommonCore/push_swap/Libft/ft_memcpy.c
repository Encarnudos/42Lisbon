/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 17:19:54 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/06 12:03:56 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*tmp_dst;
	unsigned char	*tmp_src;
	size_t			a;

	if (!dest && !src)
		return (NULL);
	a = 0;
	tmp_dst = (unsigned char *)dest;
	tmp_src = (unsigned char *)src;
	while (a < n)
	{
		tmp_dst[a] = tmp_src[a];
		a++;
	}
	return (dest);
}

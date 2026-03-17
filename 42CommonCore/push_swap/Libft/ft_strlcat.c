/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 17:41:06 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 18:03:02 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	unsigned int	a;
	unsigned int	b;
	unsigned int	dst_len;
	unsigned int	src_len;

	a = 0;
	while (dst[a])
		a++;
	dst_len = a;
	b = 0;
	while (src[b])
	{
		b++;
	}
	src_len = b;
	b = 0;
	if (size <= dst_len)
		return (size + src_len);
	while (src[b] && (dst_len + b + 1) < size)
	{
		dst[dst_len + b] = src[b];
		b++;
	}
	dst[dst_len + b] = '\0';
	return (dst_len + src_len);
}
/*
int	main(void)
{
	char	src[] = "Snoop";
	char	dst[30] = "Hello";
	size_t	size = 13;

	printf("%zu\n", ft_strlcat(dst, src, size));
	printf("%s\n", dst);
	return (0);
}
*/

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 16:00:51 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 18:31:09 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*tmp_s1;
	unsigned char	*tmp_s2;
	size_t			a;

	tmp_s1 = (unsigned char *)s1;
	tmp_s2 = (unsigned char *)s2;
	a = 0;
	if (n == 0)
		return (0);
	while (a < n)
	{
		if (tmp_s1[a] != tmp_s2[a])
			return (tmp_s1[a] - tmp_s2[a]);
		a++;
	}
	return (0);
}
/*
int	main(void)
{
	char	s1[] = "Hello Snoop";
	char	s2[] = "Hello Snooop";
	size_t	n = 3;

	int	result = ft_memcmp(s1, s2, n);
	printf("%d", result);
	return (0);
}
*/

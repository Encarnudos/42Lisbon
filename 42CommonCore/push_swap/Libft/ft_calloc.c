/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 12:59:52 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/06 12:24:39 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*tmp;

	if (nmemb == 0 || size == 0)
		return (malloc(1));
	if (nmemb > SIZE_MAX / size)
		return (NULL);
	tmp = (void *)malloc (nmemb * size);
	if (!tmp)
		return (NULL);
	ft_memset(tmp, 0, (nmemb * size));
	return (tmp);
}
/*
int	main(void)
{
	size_t	nmemb = 20;
	size_t	size = sizeof(char);
	char	*tmp = (char *)ft_calloc(nmemb, size);

	strncpy(tmp, "Hello, World!", nmemb - 1);
	tmp[nmemb - 1] = '\0';
	printf("%s\n", tmp);
	free(tmp);
	return (0);
}
*/

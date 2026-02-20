/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/25 18:30:11 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/27 01:49:31 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	size_t	a;

	if (!s)
		return (0);
	a = 0;
	while (s[a])
		a++;
	return (a);
}

char	*ft_strjoin(char *s1, char *s2)
{
	char	*s3;
	size_t	i;
	size_t	j;

	if (!s2[0])
		return (0);
	s3 = malloc(sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1 ));
	if (!s3)
		return (NULL);
	i = -1;
	while (s1[++i])
		s3[i] = s1[i];
	j = 0;
	while (s2[j])
		s3[i++] = s2[j++];
	s3[i] = '\0';
	free(s1);
	return (s3);
}

int	ft_clear(char *rest)
{
	size_t	i;
	size_t	j;
	int	next_line;

	i = 0;
	j = 0;
	next_line = 0;
	while (rest[i])
	{
		if (next_line)
			rest[j++] = rest[i];
		if (rest[i] == '\n')
			next_line = 1;
		rest[i++] = '\0';
	}
	return (next_line);
}




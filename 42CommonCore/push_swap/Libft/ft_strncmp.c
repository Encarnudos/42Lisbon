/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 17:34:15 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/03 16:20:50 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	a;

	a = 0;
	while ((s1[a] == s2[a]) && s1[a] && s2[a] && a < n)
		a++;
	if (a == n)
		return (0);
	else
		return ((unsigned char)s1[a] - (unsigned char)s2[a]);
}

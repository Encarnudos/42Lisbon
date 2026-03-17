/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 17:41:58 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 17:11:23 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *nptr)
{
	int	res;
	int	sign;
	int	a;

	res = 0;
	sign = 1;
	a = 0;
	while ((nptr[a] >= 9 && nptr[a] <= 13) || nptr[a] == 32)
		a++;
	if (nptr[a] == '+' || nptr[a] == '-')
	{
		if (nptr[a] == '-')
			sign = -1;
		a++;
	}
	while (nptr[a] >= '0' && nptr[a] <= '9')
	{
		res = (res * 10) + (nptr[a] - '0');
		a++;
	}
	return (res * sign);
}
/*
int	main(void)
{
	char	nptr[] = " 	-1234abc567";

	printf("%d\n", ft_atoi(nptr));
	return (0);
}
*/

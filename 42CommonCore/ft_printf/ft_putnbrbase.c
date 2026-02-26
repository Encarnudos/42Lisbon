/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbrbase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/04 20:36:37 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/04 20:40:55 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putnbrbase(unsigned int nbr, char format)
{
	char	*base;
	int	count;

	count = 0;
	if (format == 'x')
		base = "0123456789abcdef";
	else if (format == 'X')
		base = "0123456789ABCDEF";
	else
		return (-1);
	if (nbr >= 16)
		count += ft_putnbrbase(nbr / 16, format);
	count += ft_putchar(base[nbr % 16]);
	return (count);
}

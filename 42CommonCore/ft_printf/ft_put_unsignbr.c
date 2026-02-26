/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_unsignbr.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/04 20:31:57 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/04 20:34:15 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_put_unsignbr(unsigned int nbr)
{
	int	count;

	count = 0;
	if (nbr >= 10)
		count += ft_put_unsignbr(nbr / 10);
	count += ft_putchar((nbr % 10) + '0');
	return (count);
}

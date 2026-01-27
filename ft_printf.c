/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/04 20:05:39 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/23 20:47:44 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static	int	ft_conversion(char c, va_list args)
{
	int	count;

	count = 0;
	if (c == 'c')
		count += ft_putchar((char)va_arg(args, int));
	else if (c == 's')
		count += ft_putstr(va_arg(args, char *));
	else if (c == 'p')
		count += ft_putptr(va_arg(args, void *));
	else if (c == 'd' || c == 'i')
		count += ft_putnbr(va_arg(args, int));
	else if (c == 'u')
		count += ft_put_unsignbr(va_arg(args, unsigned int));
	else if (c == 'x')
		count += ft_putnbrbase(va_arg(args, unsigned int), c);
	else if (c == 'X')
		count += ft_putnbrbase(va_arg(args, unsigned int), c);
	else if (c == '%')
		count += ft_putchar('%');
	else
		count = -1;
	return (count);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int	count;
	size_t	i;

	count = 0;
	i = 0;
	va_start(args, format);
	if (!format)
		return(-1);
	while (format[i])
	{
		if (format[i] == '%')
		{
			if (!format[i + 1])
				return (va_end(args), -1);
			count += ft_conversion(format[++i], args);
		}
		else
			count += ft_putchar((int)format[i]);
		i++;
	}
	va_end(args);
	return (count);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 17:24:20 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/22 23:27:28 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	main(void)
{
	int	r1;
	int	r2;

	r1 = ft_printf("Hello %d\n", 42);
	r2 = printf("Hello %d\n", 42);

	printf("ft_printf returned: %d\n", r1);
	printf("printf returned: %d\n", r2);
}

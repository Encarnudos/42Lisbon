/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 15:27:38 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/13 18:39:56 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	length;
	unsigned int	a;
	char			*new_string;

	a = 0;
	if (!s || !f)
		return (NULL);
	length = ft_strlen(s);
	new_string = malloc(sizeof(char) * (length + 1));
	if (!new_string)
		return (NULL);
	while (a < length)
	{
		new_string[a] = f(a, s[a]);
		a++;
	}
	new_string[length] = '\0';
	return (new_string);
}
/*
char	ft_f(unsigned int i, char c)
{
	if(i % 2 == 0)
		return (ft_toupper(c));
	else
		return (ft_tolower(c));
}

int	main(void)
{
	char	const	s[] = "Hello Snoop"; 
	char		*nstr = ft_strmapi(s, ft_f);

	printf("%s", nstr);
	free(nstr);
	return (0);
}
*/

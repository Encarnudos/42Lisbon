/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 23:33:18 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/27 02:28:59 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{     
	static char	rest[BUFFER_SIZE + 1];
	char	*line;
	int	r_bytes;
	
	if (fd == -1 || BUFFER_SIZE < 1)
		return (NULL);
	line = ft_strjoin(0, rest);
	if (ft_clear(rest))
		return (line);
	r_bytes = read(fd, rest, BUFFER_SIZE);
	if (r_bytes < 0)
		return ((free(line), NULL));
	while (r_bytes)
	{
		line = ft_strjoin(line, rest);
		if (ft_clear(rest))
			break ;
		r_bytes = read(fd, rest, BUFFER_SIZE);
	}
	return (line);
}

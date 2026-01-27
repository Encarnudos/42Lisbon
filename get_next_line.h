/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 23:28:59 by mgracio-          #+#    #+#             */
/*   Updated: 2026/01/22 23:32:48 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <unistd.h>
# include <stdio.h>
# include <stdlib.h>

# ifndef BUFFER_SIZE
# define BUFFER_SIZE 10
# endif

size_t	ft_strlen(const char *s);
char	*ft_strjoin(char *s1, char *s2);
int	ft_clear(char *rest);
char	*get_next_line(int fd);

#endif

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgracio- <mgracio-@student.42lisboa.p      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/04 19:31:58 by mgracio-          #+#    #+#              #
#    Updated: 2026/01/04 20:49:06 by mgracio-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libftprintf.a
SRCS = ft_printf.c ft_putchar.c ft_putstr.c ft_putunsignbr.c ft_putnbr.c ft_putptr.c ft_putnbrbase.c

CC = cc
CFLAGS = -Werror -Wall -Wextra
OBJS = $(SRCS:.c=.o)
RM = rm -f

.c.o:
	$(CC) $(CFLAGS) -c $< -o $@

all: $(NAME)

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re

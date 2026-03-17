/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mgracio- <mgracio-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 15:48:12 by mgracio-          #+#    #+#             */
/*   Updated: 2025/11/17 15:26:04 by mgracio-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static	void	free_words(char **words, int b)
{
	int	a;

	a = 0;
	while (a < b)
	{
		free(words[a]);
		a++;
	}
	free(words);
}

static int	ft_count_words(const char *s, char c)
{
	int	a;
	int	words;

	a = 0;
	words = 0;
	while (s[a])
	{
		if (s[a] != c)
		{
			words++;
			while (s[a] && s[a] != c)
				a++;
		}
		else
			a++;
	}
	return (words);
}

static char	*word_splitter(const char *s, char c)
{
	char	*word;
	int		a;

	a = 0;
	while (s[a] && s[a] != c)
		a++;
	word = (char *) malloc(sizeof(char) * (a + 1));
	if (!word)
		return (NULL);
	a = 0;
	while (s[a] && s[a] != c)
	{
		word[a] = s[a];
		a++;
	}
	word[a] = '\0';
	return (word);
}

static	int	fill_words(const char *s, char c, char **words)
{
	int	a;
	int	b;

	a = 0;
	b = 0;
	while (s[a])
	{
		if (s[a] != c)
		{
			words[b] = word_splitter(&s[a], c);
			if (!words[b++])
				return (free_words(words, b), 0);
			while (s[a] && s[a] != c)
				a++;
		}
		else
			a++;
	}
	words[b] = NULL;
	return (1);
}

char	**ft_split(char const *s, char c)
{
	char	**words;

	if (!s)
		return (NULL);
	words = (char **) malloc(sizeof(char *) * (ft_count_words(s, c) + 1));
	if (!words)
		return (NULL);
	if (!fill_words(s, c, words))
		return (NULL);
	return (words);
}
/*
int	main(void)
{
	char const	s[] = "Hello,Snoop,Encarnacao";
	char	c = ',';
	char	**words = ft_split(s, c);
	int	a = 0;

	for (a = 0; words[a] != NULL; a++)
	{
		printf("%s\n", words[a]);
		free(words[a]);
	}
	free(words);
	return (0);
}
*/

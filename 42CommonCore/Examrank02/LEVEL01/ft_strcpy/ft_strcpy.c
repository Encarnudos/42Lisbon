/*
Assignment name  : ft_strcpy
Expected files   : ft_strcpy.c
Allowed functions: 
--------------------------------------------------------------------------------

Reproduce the behavior of the function strcpy (man strcpy).

Your function must be declared as follows:

char    *ft_strcpy(char *dst, char *src);
*/

#include <stdio.h>

char    *ft_strcpy(char *dst, char *src)
{
    int i;
    
    i = 0;
    while (src[i])
    {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';
    return (dst);
}

int main(void)
{
    char dst[50];
    char *src;

    src = "eu sou o miguel";
    ft_strcpy(dst, src);
    printf("%s\n", dst);

    return(0);
}
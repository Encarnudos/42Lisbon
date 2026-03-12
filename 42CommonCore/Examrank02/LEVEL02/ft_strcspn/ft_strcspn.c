/* Assignment name	: ft_strcspn
Expected files	: ft_strcspn.c
Allowed functions: None
---------------------------------------------------------------

Reproduce exactly the behavior of the function strcspn
(man strcspn).

The function should be prototyped as follows:

size_t	ft_strcspn(const char *s, const char *reject); */

#include <stddef.h>
#include <stdio.h>
#include <string.h>

size_t  ft_strcspn(const char *s, const char *reject)
{
    size_t count;

    count = 0;
    while (*s)
    {
        const char *p = reject;
        while (*p)
        {
            if (*p == *s)
                return count;
            p++;
        }
        count++;
        s++;
    }
    return count;
}

int main(void)
{
    const char *s1 = "hello world";
    const char *r1 = " ";
    
    const char *s2 = "42 Network";
    const char *r2 = "xyz";

    const char *s3 = "abcdef";
    const char *r3 = "d";

    const char *s4 = "";
    const char *r4 = "abc";

    printf("Test 1:\n");
    printf("ft_strcspn: %zu\n", ft_strcspn(s1, r1));
    printf("strcspn   : %zu\n\n", strcspn(s1, r1));

    printf("Test 2:\n");
    printf("ft_strcspn: %zu\n", ft_strcspn(s2, r2));
    printf("strcspn   : %zu\n\n", strcspn(s2, r2));

    printf("Test 3:\n");
    printf("ft_strcspn: %zu\n", ft_strcspn(s3, r3));
    printf("strcspn   : %zu\n\n", strcspn(s3, r3));

    printf("Test 4:\n");
    printf("ft_strcspn: %zu\n", ft_strcspn(s4, r4));
    printf("strcspn   : %zu\n\n", strcspn(s4, r4));

    return 0;
}
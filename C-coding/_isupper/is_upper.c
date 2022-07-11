#include "main.h"
/**
 * _isupper - checks for uppercase characters.
 * @c: the variable to be checked.
 * Return: 1 if uppercase
 * Return: 0 if otherwise
 */

int _isupper(int c)
{
    if (c >= 'a' && c <= 'z')
        return (1);
    else
        return (0);
}
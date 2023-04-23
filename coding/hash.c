#include <stdio.h>
#include <stdlib.h>

#define TAB_MAX 10000

unsigned long int sdbm( char *word );

int main()
{   
    char word[100];
    printf("Word to hash\n");
    scanf("%s",word);

    sdbm(word);
}


unsigned long int sdbm( char *word )
{
     unsigned long h, i;
    i = 0;
    h = 5347;

    while(word[i])
    {
        h *= (31);
        h ^= word[i++];
        h &= 0xffffffff; // consideram-se apenas 32 bits 
    }

    printf("%lu\n",h % TAB_MAX);
    return h;
}
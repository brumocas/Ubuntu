#include <stdio.h>

int next_prime2(int n);
int checkPrimeNumber2(int n);

int main()
{
    int number  = 2;
    int res = next_prime2(number);
    printf("%i\n",res);
}

int next_prime2(int n)
{   int i,k;

    if(checkPrimeNumber2(n))
    return n;

    for ( i = n + 1 ;; i++)
    {
        for ( k  = 2 ; k < i ; k++)
        {
            if (i % k==0)
            break;
        }
        if (i==k)
        break;
        
    }
    return i;
}

int checkPrimeNumber2(int n)
{
    int j, flag = 1;
    for (j = 2; j <= n / 2; ++j) {
        if (n % j == 0) {
            flag = 0;
            break;
        }
    }
    return flag;
}
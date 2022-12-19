#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);

    char a, b, c, d;

    a = getchar();
    b = getchar();
    c = getchar();
    d = getchar();

    int i = 4;

    while (true)
    {
        if (c == d)
        {
            a = d;
            b = getchar();
            c = getchar();
            d = getchar();
            i += 3;
        }
        else if (b == d || b == c)
        {
            a = c;
            b = d;
            c = getchar();
            d = getchar();
            i += 2;
        }
        else if (a == d || a == c || a == b)
        {
            a = b;
            b = c;
            c = d;
            d = getchar();
            ++i;
        }
        else
            break;
    }

    std::cout << i << std::endl;
}
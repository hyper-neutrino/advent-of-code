#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);

    int a, b, x, y;

    int count = 0;

    while (std::scanf("%d-%d,%d-%d", &a, &b, &x, &y) != -1)
    {
        if (a <= x && b >= y || x <= a && y >= b)
            ++count;
    }

    std::cout << count << std::endl;
}
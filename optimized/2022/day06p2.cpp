#include <deque>
#include <iostream>

int main()
{
    std::ios_base::sync_with_stdio(false);

    int c[123]{0};
    int d = 0;
    std::deque<char> seq;

    for (int i = 0; i < 14; ++i)
    {
        char k = getchar();

        ++c[k];
        if (c[k] == 2)
            ++d;

        seq.push_back(k);
    }

    int i = 14;

    while (d)
    {
        ++i;

        char k = seq.front();

        seq.pop_front();

        --c[k];
        if (c[k] == 1)
            --d;

        k = getchar();

        ++c[k];
        if (c[k] == 2)
            ++d;

        seq.push_back(k);
    }

    std::cout << i << std::endl;
}
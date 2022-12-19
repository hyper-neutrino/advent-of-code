#include <cstring>
#include <iostream>
#include <string>

int main()
{
    std::ios_base::sync_with_stdio(false);

    int total = 0;
    std::string s;

    __uint128_t b = 0;

    while (getline(std::cin, s))
    {
        int k = s.length() / 2;

        for (int i = 0; i < k; ++i)
        {
            b |= 1ull << s[i];
        }

        while (true)
        {
            if (b & (1ull << s[k]))
            {
                total += s[k] <= 'Z' ? s[k] - 38 : s[k] - 96;
                b = 0;
                break;
            }
            ++k;
        }
    }

    std::cout << total << std::endl;
}
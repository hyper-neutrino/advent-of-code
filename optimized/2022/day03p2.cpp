#include <iostream>
#include <string>

int main()
{
    std::ios_base::sync_with_stdio(false);

    int total = 0;
    std::string s;

    __uint128_t b1 = 0;
    __uint128_t b2 = 0;

    while (getline(std::cin, s))
    {
        for (char c : s)
        {
            b1 |= 1ull << c;
        }

        getline(std::cin, s);
        for (char c : s)
        {
            b2 |= 1ull << c;
        }

        b1 &= b2;

        getline(std::cin, s);
        for (char c : s)
        {
            if (b1 & (1ull << c))
            {
                total += c <= 'Z' ? c - 38 : c - 96;
                b1 = 0;
                b2 = 0;
                break;
            }
        }
    }

    std::cout << total << std::endl;
}
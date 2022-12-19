#include <iostream>
#include <string>

#define step                                \
    std::cout << crt[abs(i % 40 - x) <= 1]; \
    if (++i % 40 == 0)                      \
        std::cout << std::endl;

int main()
{
    std::ios_base::sync_with_stdio(false);

    int x = 1;
    int i = 0;

    std::string s;

    char crt[2]{'.', '#'};

    int t = 0;

    while (getline(std::cin, s))
    {
        step;

        if (s[0] == 'a')
        {
            step;
            x += stoi(s.substr(s.find(' ') + 1));
        }
    }

    std::cout << t << std::endl;
}
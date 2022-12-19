#include <iostream>
#include <string>

#define step            \
    if (++i % 40 == 20) \
        t += i * x;

int main()
{
    std::ios_base::sync_with_stdio(false);

    int x = 1;
    int i = 0;

    std::string s;

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
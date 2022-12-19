#include <iostream>
#include <string>

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::string s;

    int m = 0, c = 0;

    while (getline(std::cin, s))
    {

        if (s.length() == 0)
        {
            if (c > m)
                m = c;
            c = 0;
        }
        else
        {
            c += std::stoi(s);
        }
    }

    if (c > m)
        m = c;

    std::cout << m << std::endl;
}
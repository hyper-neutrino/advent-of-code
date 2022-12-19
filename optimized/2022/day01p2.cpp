#include <iostream>
#include <string>

void shift(int c, int &m1, int &m2, int &m3)
{
    if (c > m1)
    {
        if (c > m2)
        {
            if (c > m3)
            {
                m1 = m2;
                m2 = m3;
                m3 = c;
            }
            else
            {
                m1 = m2;
                m2 = c;
            }
        }
        else
        {
            m1 = c;
        }
    }
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::string s;

    int m1 = 0, m2 = 0, m3 = 0, c = 0;

    while (getline(std::cin, s))
    {
        if (s.length() == 0)
        {
            shift(c, m1, m2, m3);
            c = 0;
        }
        else
        {
            c += std::stoi(s);
        }
    }

    shift(c, m1, m2, m3);

    std::cout << m1 + m2 + m3 << std::endl;
}
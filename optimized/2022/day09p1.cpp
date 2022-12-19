#include <iostream>
#include <set>
#include <utility>

inline int sign(int a, int b)
{
    return a < b ? -1 : a > b ? 1
                              : 0;
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::pair<int, int> head{0, 0};
    std::pair<int, int> tail{0, 0};

    char c;
    int x;

    int dxs[86]{0};
    int dys[86]{0};

    dxs['R'] = 1;
    dxs['L'] = -1;

    dys['U'] = 1;
    dys['D'] = -1;

    std::set<std::pair<int, int>> positions;

    while (scanf("%c %d\n", &c, &x) != EOF)
    {
        while (x--)
        {
            head.first += dxs[c];
            head.second += dys[c];

            if (abs(head.first - tail.first) >= 2 || abs(head.second - tail.second) >= 2)
            {
                tail.first += sign(head.first, tail.first);
                tail.second += sign(head.second, tail.second);
            }

            positions.insert(tail);
        }
    }

    std::cout << positions.size() << std::endl;
}
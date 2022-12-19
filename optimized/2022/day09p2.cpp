#include <cstring>
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

    std::pair<int, int> rope[10];
    memset(rope, 0, 10 * sizeof(std::pair<int, int>));

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
            rope[0].first += dxs[c];
            rope[0].second += dys[c];

            for (int i = 0; i < 9; ++i)
            {
                if (abs(rope[i].first - rope[i + 1].first) >= 2 || abs(rope[i].second - rope[i + 1].second) >= 2)
                {
                    rope[i + 1].first += sign(rope[i].first, rope[i + 1].first);
                    rope[i + 1].second += sign(rope[i].second, rope[i + 1].second);
                }
            }

            positions.insert(rope[9]);
        }
    }

    std::cout << positions.size() << std::endl;
}
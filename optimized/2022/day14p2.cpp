#include <iostream>
#include <map>
#include <deque>
#include <set>
#include <string>
#include <utility>

int main()
{
    std::set<std::pair<int, int>> grid;

    std::string s;
    int i, j, x1, y1, x2, y2;

    int abyss = 0;

    while (getline(std::cin, s))
    {
        i = s.find(',');
        x1 = stoi(s.substr(0, i));
        j = s.find(' ', i);
        y1 = stoi(s.substr(i + 1, j - i));

        while (true)
        {
            i = s.find(' ', j + 1) + 1;
            j = s.find(',', i);
            x2 = stoi(s.substr(i, j - i));
            i = j + 1;
            j = s.find(' ', i);
            y2 = stoi(s.substr(i, j - i));

            int mx = std::min(x1, x2);
            int Mx = x1 + x2 - mx;
            int my = std::min(y1, y2);
            int My = y1 + y2 - my;

            abyss = std::max(abyss, My);

            for (int x = mx; x <= Mx; ++x)
                for (int y = my; y <= My; ++y)
                    grid.insert({x, y});

            if (j == -1)
                break;

            x1 = x2;
            y1 = y2;
        }
    }

    int total = 0;
    int x, y;

    std::deque<std::pair<int, int>> positions{{500, 0}};

    while (!positions.empty())
    {
        x = positions.back().first;
        y = positions.back().second;

        while (true)
        {
            if (y > abyss)
                goto end;

            if (grid.count({x, y + 1}) == 0)
                ;
            else if (grid.count({x - 1, y + 1}) == 0)
                --x;
            else if (grid.count({x + 1, y + 1}) == 0)
                ++x;
            else
                goto end;

            ++y;
            positions.push_back({x, y});
            continue;

        end:
            grid.insert({x, y});
            positions.pop_back();
            ++total;
            break;
        }
    }

    std::cout << total << std::endl;
}

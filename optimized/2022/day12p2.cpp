#include <cstring>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

struct state
{
    int row, col, cost;
};

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::vector<std::string> grid;
    std::string s;

    int sr = -1, sc, er = -1, ec, cr = 0;

    while (getline(std::cin, s))
    {
        if (sr == -1 && (sc = s.find('S')) != -1)
        {
            sr = cr;
            s[sc] = 'a';
        }

        if (er == -1 && (ec = s.find('E')) != -1)
        {
            er = cr;
            s[ec] = 'z';
        }

        grid.push_back(s);
        ++cr;
    }

    bool seen[grid.size()][grid[0].length()];
    memset(seen, 0, grid.size() * grid[0].length());
    seen[0][0] = true;

    std::queue<struct state *> q;
    q.push(new state{er, ec, 0});

    while (!q.empty())
    {
        struct state *s = q.front();
        q.pop();

        int rs[4]{s->row - 1, s->row + 1, s->row, s->row};
        int cs[4]{s->col, s->col, s->col - 1, s->col + 1};

        for (int i = 0; i < 4; ++i)
        {
            if (rs[i] < 0 || cs[i] < 0 || rs[i] >= grid.size() || cs[i] >= grid[0].length())
                continue;

            if (seen[rs[i]][cs[i]])
                continue;

            if (grid[rs[i]][cs[i]] - grid[s->row][s->col] < -1)
                continue;

            if (grid[rs[i]][cs[i]] == 'a')
            {
                std::cout << s->cost + 1 << std::endl;
                return 0;
            }

            seen[rs[i]][cs[i]] = true;
            q.push(new state{rs[i], cs[i], s->cost + 1});
        }
    }
}
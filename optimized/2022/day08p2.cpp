#include <cstring>
#include <iostream>
#include <vector>

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::vector<std::vector<int>> grid;
    grid.emplace_back();

    char c;
    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
            grid.emplace_back();
        else
            grid.back().push_back(c - 48);
    }

    grid.pop_back();

    int score[grid.size() - 1][grid[0].size() - 1];

    int m[10]{0};

    for (int r = 1; r < grid.size() - 1; ++r)
    {
        memset(m, 0, 10 * sizeof(int));

        for (int c = 1; c < grid[r].size() - 1; ++c)
        {
            score[r][c] = c - m[grid[r][c]];
            for (int j = 0; j <= grid[r][c]; ++j)
                m[j] = c;
        }

        int k = grid[r].size() - 1;
        for (int i = 0; i < 10; ++i)
            m[i] = k;

        for (int c = grid[r].size() - 2; c > 0; --c)
        {
            score[r][c] *= m[grid[r][c]] - c;
            for (int j = 0; j <= grid[r][c]; ++j)
                m[j] = c;
        }
    }

    for (int c = 1; c < grid[0].size() - 1; ++c)
    {
        memset(m, 0, 10 * sizeof(int));

        for (int r = 1; r < grid.size() - 1; ++r)
        {
            score[r][c] *= r - m[grid[r][c]];
            for (int j = 0; j <= grid[r][c]; ++j)
                m[j] = r;
        }

        int k = grid.size() - 1;
        for (int i = 0; i < 10; ++i)
            m[i] = k;

        for (int r = grid.size() - 2; r > 0; --r)
        {
            score[r][c] *= m[grid[r][c]] - r;
            for (int j = 0; j <= grid[r][c]; ++j)
                m[j] = r;
        }
    }

    int t = 0;

    for (int r = 1; r < grid.size() - 1; ++r)
    {
        for (int c = 1; c < grid[r].size() - 1; ++c)
        {
            if (score[r][c] > t)
                t = score[r][c];
        }
    }

    std::cout << t << std::endl;
}

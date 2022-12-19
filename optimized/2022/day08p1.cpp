#include <iostream>
#include <vector>

#define check                 \
    if (grid[r][c] > m)       \
    {                         \
        visible[r][c] = true; \
        m = grid[r][c];       \
        if (m == 9)           \
            break;            \
    }

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

    bool visible[grid.size()][grid[0].size()]{0};

    for (int r = 0; r < grid.size(); ++r)
    {
        int m = -1;
        for (int c = 0; c < grid[r].size(); ++c)
            check;

        m = -1;
        for (int c = grid[r].size() - 1; c >= 0; --c)
            check;
    }

    for (int c = 0; c < grid[0].size(); ++c)
    {
        int m = -1;
        for (int r = 0; r < grid.size(); ++r)
            check;

        m = -1;
        for (int r = grid.size() - 1; r >= 0; --r)
            check;
    }

    int t = 0;

    for (int r = 0; r < grid.size(); ++r)
    {
        for (int c = 0; c < grid[r].size(); ++c)
        {
            t += visible[r][c];
        }
    }

    std::cout << t << std::endl;
}

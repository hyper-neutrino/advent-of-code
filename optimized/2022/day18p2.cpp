#include <climits>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>

std::tuple<int, int, int> neighbors[]{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}, {-1, 0, 0}, {0, -1, 0}, {0, 0, -1}};

int main()
{
    std::set<std::tuple<int, int, int>> points;

    int mx, my, mz, Mx, My, Mz;
    mx = my = mz = INT_MAX;
    Mx = My = Mz = INT_MIN;

    int x, y, z;
    while (std::scanf("%d,%d,%d\n", &x, &y, &z) != EOF)
    {
        points.insert({x, y, z});

        if (x < mx)
            mx = x;
        if (y < my)
            my = y;
        if (z < mz)
            mz = z;

        if (x > Mx)
            Mx = x;
        if (y > My)
            My = y;
        if (z > Mz)
            Mz = z;
    }

    --mx;
    --my;
    --mz;

    ++Mx;
    ++My;
    ++Mz;

    std::vector<std::tuple<int, int, int>> stack{{mx, my, mz}};
    std::set<std::tuple<int, int, int>> visited{{mx, my, mz}};
    int total = 0;

    while (!stack.empty())
    {
        std::tuple<int, int, int> point = stack.back();
        stack.pop_back();

        for (int i = 0; i < 6; i++)
        {
            std::tuple<int, int, int> neighbor{std::get<0>(point) + std::get<0>(neighbors[i]), std::get<1>(point) + std::get<1>(neighbors[i]), std::get<2>(point) + std::get<2>(neighbors[i])};
            std::tie(x, y, z) = neighbor;

            if (x < mx || x > Mx || y < my || y > My || z < mz || z > Mz)
                continue;

            if (points.count(neighbor) > 0)
            {
                ++total;
                continue;
            }

            if (visited.count(neighbor) > 0)
                continue;

            visited.insert(neighbor);
            stack.push_back(neighbor);
        }
    }

    std::cout << total << std::endl;
}
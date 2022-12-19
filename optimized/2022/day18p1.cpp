#include <iostream>
#include <set>
#include <tuple>
#include <vector>

std::tuple<int, int, int> neighbors[]{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}, {-1, 0, 0}, {0, -1, 0}, {0, 0, -1}};

int main()
{
    std::set<std::tuple<int, int, int>> points;

    int x, y, z;
    while (std::scanf("%d,%d,%d\n", &x, &y, &z) != EOF)
        points.insert({x, y, z});

    int total = 0;

    for (std::tuple<int, int, int> point : points)
    {
        for (int i = 0; i < 6; i++)
        {
            if (points.count({std::get<0>(point) + std::get<0>(neighbors[i]), std::get<1>(point) + std::get<1>(neighbors[i]), std::get<2>(point) + std::get<2>(neighbors[i])}) == 0)
                ++total;
        }
    }

    std::cout << total << std::endl;
}
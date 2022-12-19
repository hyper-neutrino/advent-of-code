#include <iostream>
#include <utility>
#include <vector>

int L = 4000000;

int main()
{
    std::vector<int> up_edges, dn_edges;
    std::vector<std::pair<std::pair<int, int>, int>> sensors;

    int sx, sy, bx, by, r;
    uint64_t x, y;

    while (std::scanf("Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d\n", &sx, &sy, &bx, &by) != EOF)
    {
        r = abs(sx - bx) + abs(sy - by);
        sensors.push_back({{sx, sy}, r});

        up_edges.push_back(sy - sx + r + 1);
        up_edges.push_back(sy - sx - r - 1);

        dn_edges.push_back(sx + sy + r + 1);
        dn_edges.push_back(sx + sy - r - 1);
    }

    for (int a : up_edges)
    {
        for (int b : dn_edges)
        {
            if ((a + b) % 2)
                continue;

            x = (b - a) / 2;
            y = (b + a) / 2;

            if (x < 0 || x > L || y < 0 || y > L)
                goto end;

            for (std::pair<std::pair<int, int>, int> &sensor : sensors)
                if (abs(x - sensor.first.first) + abs(y - sensor.first.second) <= sensor.second)
                    goto end;

            std::cout << x * 4000000 + y << std::endl;
            return 0;

        end:;
        }
    }
}
#include <algorithm>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

int Y = 2000000;

int main()
{
    std::vector<std::pair<int, int>> intervals;
    std::set<int> exclude_;

    int sx, sy, bx, by, o;

    while (std::scanf("Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d\n", &sx, &sy, &bx, &by) != EOF)
    {
        if (by == Y)
            exclude_.insert(bx);

        o = abs(sx - bx) + abs(sy - by) - abs(sy - Y);

        if (o < 0)
            continue;

        intervals.push_back({sx - o, sx + o});
    }

    std::vector<int> exclude;
    for (int x : exclude_)
        exclude.push_back(x);

    std::sort(intervals.begin(), intervals.end());
    std::sort(exclude.begin(), exclude.end());
    std::pair<int, int> interval = intervals.front();

    int ei = 0;
    int total = 0;

    for (std::pair<int, int> next : intervals)
    {
        if (next.first - interval.second <= 1)
        {
            interval.second = std::max(interval.second, next.second);
        }
        else
        {
            total += interval.second - interval.first + 1;

            while (ei < exclude.size())
            {
                if (exclude[ei] > interval.second)
                    break;

                if (exclude[ei++] >= interval.first)
                    --total;
            }

            interval = next;
        }
    }

    total += interval.second - interval.first + 1;

    while (ei < exclude.size())
    {
        if (exclude[ei] > interval.second)
            break;

        if (exclude[ei++] >= interval.first)
            --total;
    }

    std::cout << total << std::endl;
}
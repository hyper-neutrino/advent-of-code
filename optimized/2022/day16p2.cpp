#include <cstring>
#include <deque>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

int dfs(std::unordered_map<int, std::unordered_map<int, int>> *cache, int *flowmap, std::vector<std::pair<int, int>> *neighbors, int time, int valve, int bitmask)
{
    if (cache[time][valve].count(bitmask) > 0)
        return cache[time][valve][bitmask];

    int maxval = 0, remtime, bit;

    for (std::pair<int, int> neighbor : neighbors[valve])
    {
        remtime = time - neighbor.second - 1;

        if (remtime <= 0)
            continue;

        bit = 1 << neighbor.first;

        if (bitmask & bit)
            continue;

        maxval = std::max(maxval, dfs(cache, flowmap, neighbors, remtime, neighbor.first, bitmask | bit) + flowmap[neighbor.first] * remtime);
    }

    return cache[time][valve][bitmask] = maxval;
}

int main()
{
    std::unordered_map<std::string, int> flows;
    std::unordered_map<std::string, std::vector<std::string>> tunnels;

    std::string s, v;
    int i, j;

    while (getline(std::cin, s))
    {
        std::vector<std::string> targets;
        v = s.substr(s.find(' ', s.find("to") + 3) + 1);
        i = 0;

        while ((j = v.find(',', i + 1)) != -1)
        {
            targets.push_back(v.substr(i, j - i));
            i = j + 2;
        }

        targets.push_back(v.substr(i));

        i = s.find(' ') + 1;
        v = s.substr(i, s.find(' ', i) - i);

        i = s.find('=') + 1;
        i = stoi(s.substr(i, s.find(';') - i));

        flows[v] = i;
        tunnels[v] = targets;
    }

    std::unordered_map<std::string, std::unordered_map<std::string, int>> dists;
    std::unordered_map<std::string, int> indices;

    i = 0;

    for (const std::pair<std::string, int> &valve : flows)
    {
        if (valve.first != "AA" && valve.second == 0)
            continue;

        if (valve.first != "AA")
            indices[valve.first] = i++;

        std::unordered_set<std::string> visited;
        std::deque<std::pair<int, std::string>> queue{{0, valve.first}};

        while (!queue.empty())
        {
            std::pair<int, std::string> current = queue.front();
            queue.pop_front();

            for (std::string neighbor : tunnels[current.second])
            {
                if (visited.count(neighbor) > 0)
                    continue;

                visited.insert(neighbor);
                if (flows[neighbor] > 0)
                    dists[valve.first][neighbor] = current.first + 1;

                queue.push_back({current.first + 1, neighbor});
            }
        }

        dists[valve.first].erase(valve.first);
        dists[valve.first].erase("AA");
    }

    indices["AA"] = i++;

    std::vector<std::pair<int, int>> neighbors[i];
    int flowmap[i];

    for (const std::pair<std::string, std::unordered_map<std::string, int>> &x : dists)
    {
        int xi = indices[x.first];
        flowmap[xi] = flows[x.first];
        for (const std::pair<std::string, int> &y : x.second)
        {
            neighbors[xi].push_back({indices[y.first], y.second});
        }
    }

    std::unordered_map<int, std::unordered_map<int, int>> cache[27];

    int k = 1 << (i - 1);
    int k2 = k - 1;

    int maxval = 0;

    for (int b = (k >> 1) - 1; b >= 0; --b)
        maxval = std::max(maxval, dfs(cache, flowmap, neighbors, 26, i - 1, b) + dfs(cache, flowmap, neighbors, 26, i - 1, k2 ^ b));

    std::cout << maxval << std::endl;
}
#include <iostream>
#include <map>
#include <tuple>

#define step(a, b, c, d)                                                                                                                                       \
    remtime = time - wait;                                                                                                                                     \
    if (remtime > 0)                                                                                                                                           \
    {                                                                                                                                                          \
        maxval = std::max(maxval, dfs(remtime, ore_bots + a, clay_bots + b, obs_bots + c,                                                                      \
                                      std::min(ore_max * remtime, ore + ore_bots * wait - ore_cost * a - clay_cost * b - obs_cost_ore * c - geo_cost_ore * d), \
                                      std::min(obs_cost_clay * remtime, clay + clay_bots * wait - obs_cost_clay * c),                                          \
                                      std::min(geo_cost_obs * remtime, obs + obs_bots * wait - geo_cost_obs * d)) +                                            \
                                      d * remtime);                                                                                                            \
    }

typedef std::tuple<int, int, int, int, int, int, int> state;

int ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geo_cost_ore, geo_cost_obs;
int ore_max;
std::map<state, int> cache;

int dfs(int time, int ore_bots, int clay_bots, int obs_bots, int ore, int clay, int obs)
{
    if (time == 0)
        return 0;

    state key{time, ore_bots, clay_bots, obs_bots, ore, clay, obs};

    if (cache.count(key) > 0)
        return cache[key];

    int maxval = 0, wait, remtime;

    if (ore_bots < ore_max)
    {
        wait = std::max(0, (ore_cost - ore + ore_bots - 1) / ore_bots) + 1;
        step(1, 0, 0, 0);
    }

    if (clay_bots < obs_cost_clay)
    {
        wait = std::max(0, (clay_cost - ore + ore_bots - 1) / ore_bots) + 1;
        step(0, 1, 0, 0);
    }

    if (obs_bots < geo_cost_obs && clay_bots)
    {
        wait = std::max(0, std::max((obs_cost_ore - ore + ore_bots - 1) / ore_bots, (obs_cost_clay - clay + clay_bots - 1) / clay_bots)) + 1;
        step(0, 0, 1, 0);
    }

    if (obs_bots)
    {
        wait = std::max(0, std::max((geo_cost_ore - ore + ore_bots - 1) / ore_bots, (geo_cost_obs - obs + obs_bots - 1) / obs_bots)) + 1;
        step(0, 0, 0, 1);
    }

    return maxval;
}

int main()
{
    int total = 0;
    int i;

    while (std::scanf("Blueprint %d: Each ore robot costs %d ore. Each clay robot costs %d ore. Each obsidian robot costs %d ore and %d clay. Each geode robot costs %d ore and %d obsidian.\n",
                      &i, &ore_cost, &clay_cost, &obs_cost_ore, &obs_cost_clay, &geo_cost_ore, &geo_cost_obs) != EOF)
    {
        ore_max = std::max(std::max(ore_cost, clay_cost), std::max(obs_cost_ore, geo_cost_ore));
        cache.clear();
        total += i * dfs(24, 1, 0, 0, 0, 0, 0);
    }

    std::cout << total << std::endl;
}
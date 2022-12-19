#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::vector<std::string> path;
    std::unordered_map<std::string, int> fs;

    std::string s;

    while (getline(std::cin, s))
    {
        if (s[0] == '$')
        {
            if (s[2] == 'c')
            {
                if (s[5] == '/')
                {
                    path.clear();
                    path.push_back("/");
                }
                else if (s[5] == '.')
                {
                    path.pop_back();
                }
                else
                {
                    path.push_back(path.back() + s.substr(5) + "/");
                }
            }
        }
        else if (s[0] != 'd')
        {
            int i = s.find(' ');
            int x = stoi(s.substr(0, i));

            for (std::string sub : path)
            {
                fs[sub] += x;
            }
        }
    }

    int t = 0;

    for (auto x : fs)
    {
        if (x.second <= 100000)
            t += x.second;
    }

    std::cout << t << std::endl;
}
#include <deque>
#include <iostream>
#include <string>

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::string s;
    getline(std::cin, s);

    int N = s.length() / 4 + 2;
    std::deque<char> stacks[N];

    do
    {
        if (s.length() == 0)
        {
            break;
        }

        for (int i = 1; i < N; ++i)
        {
            char c = s[i * 4 - 3];
            if (c != ' ')
                stacks[i].push_front(c);
        }
    } while (getline(std::cin, s));

    for (int i = 1; i < N; ++i)
        stacks[i].pop_front();

    int amt, src, dest;

    while (scanf("move %d from %d to %d\n", &amt, &src, &dest) != EOF)
    {
        for (int i = stacks[src].size() - amt; i < stacks[src].size(); ++i)
            stacks[dest].push_back(stacks[src][i]);

        while (amt--)
            stacks[src].pop_back();
    }

    for (int i = 1; i < N; ++i)
    {
        std::cout << stacks[i].back();
    }

    std::cout << std::endl;
}
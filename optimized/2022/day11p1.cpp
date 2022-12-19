#include <iostream>
#include <queue>
#include <vector>

struct monkey
{
    std::queue<int> items;
    bool op_is_add = false;
    int other_arg;
    bool selfie = false;
    int count = 0;
    int test, iftrue, iffalse;
};

int main()
{
    std::ios_base::sync_with_stdio(false);

    std::vector<struct monkey> monkeys;
    std::string s, t;
    char op;

    int i, n;

    while (getline(std::cin, s))
    {
        monkeys.emplace_back();

        getline(std::cin, s);

        i = s.find(':') + 2;
        n = s.find(',', i);

        while (n != -1)
        {
            monkeys.back().items.push(stoi(s.substr(i, n - i)));

            i = n + 2;
            n = s.find(',', i);
        }

        monkeys.back().items.push(stoi(s.substr(i)));

        getline(std::cin, s);

        n = s.find(' ', s.find('=') + 2);

        monkeys.back().op_is_add = s[n + 1] & 1;

        if (s[n + 3] == 'o')
            monkeys.back().selfie = true;
        else
            monkeys.back().other_arg = stoi(s.substr(n + 3));

        getline(std::cin, s);

        monkeys.back().test = stoi(s.substr(s.find_last_of(' ') + 1));

        getline(std::cin, s);

        monkeys.back().iftrue = stoi(s.substr(s.find_last_of(' ') + 1));

        getline(std::cin, s);

        monkeys.back().iffalse = stoi(s.substr(s.find_last_of(' ') + 1));

        getline(std::cin, s);
    }

    for (i = 0; i < 20; ++i)
    {
        for (struct monkey &monkey : monkeys)
        {
            while (!monkey.items.empty())
            {
                ++monkey.count;

                int item = monkey.items.front();
                monkey.items.pop();

                int other = monkey.selfie ? item : monkey.other_arg;

                if (monkey.op_is_add)
                    item += other;
                else
                    item *= other;

                item /= 3;

                monkeys[item % monkey.test ? monkey.iffalse : monkey.iftrue].items.push(item);
            }
        }
    }

    int m1 = 0, m2 = 0;

    for (struct monkey &monkey : monkeys)
    {
        if (monkey.count > m1)
        {
            m2 = m1;
            m1 = monkey.count;
        }
        else if (monkey.count > m2)
            m2 = monkey.count;
    }

    std::cout << m1 * m2 << std::endl;
}
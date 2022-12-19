#include <iostream>
#include <string>
#include <vector>

struct signal
{
    enum
    {
        INT,
        LIST
    } type;

    union
    {
        int i;
        std::vector<struct signal *> *v;
    };

    ~signal()
    {
        if (this->type == signal::LIST)
            this->v->~vector();
    }
};

struct signal *isignal(int x)
{
    struct signal *s = new struct signal;
    s->type = signal::INT;
    s->i = x;
    return s;
}

struct signal *parse(std::string line, int &i)
{
    struct signal *s = new struct signal;

    if (line[i] == '[')
    {
        s->type = signal::LIST;
        s->v = new std::vector<struct signal *>;

        ++i;

        while (line[i] != ']')
        {
            s->v->push_back(parse(line, i));

            if (line[i] == ',')
                ++i;
        }

        ++i;
    }
    else
    {
        s->type = signal::INT;
        s->i = line[i] - 48;

        while (line[++i] >= 48 && line[i] < 58)
        {
            s->i = s->i * 10 + line[i] - 48;
        }
    }

    return s;
}

struct signal *wrap(struct signal *x)
{
    struct signal *s = new struct signal;

    s->type = signal::LIST;
    s->v = new std::vector<struct signal *>{x};

    return s;
}

int cmp(struct signal *s, struct signal *t)
{
    if (s->type == signal::INT)
    {
        if (t->type == signal::INT)
            return s->i - t->i;

        return cmp(wrap(s), t);
    }
    else
    {
        if (t->type == signal::INT)
            return cmp(s, wrap(t));

        int k;
        int c = std::min(s->v->size(), t->v->size());

        for (int i = 0; i < c; ++i)
        {
            if (k = cmp(s->v->at(i), t->v->at(i)))
                return k;
        }

        return s->v->size() - t->v->size();
    }
}

int main()
{
    std::string s;

    int t2 = 1;
    int t6 = 2;

    struct signal *s2 = wrap(wrap(isignal(2)));
    struct signal *s6 = wrap(wrap(isignal(6)));
    struct signal *k;

    int i;

    while (getline(std::cin, s))
    {
        if (s.length() == 0)
            continue;

        k = parse(s, i = 0);

        if (cmp(k, s2) < 0)
        {
            ++t2;
            ++t6;
        }
        else if (cmp(k, s6) < 0)
            ++t6;
    }

    std::cout << t2 * t6 << std::endl;
}
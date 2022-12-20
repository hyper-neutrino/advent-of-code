#include <iostream>
#include <vector>

struct Node
{
    int n;
    struct Node *left, *right;
};

int main()
{
    std::vector<struct Node *> nodes;
    int x;

    while (std::cin >> x)
    {
        nodes.push_back(new Node{x});
    }

    int n = nodes.size();

    for (int i = 0; i < n; ++i)
    {
        nodes[i]->right = nodes[(i + 1) % n];
        nodes[i]->left = nodes[(i + n - 1) % n];
    }

    struct Node *z;

    for (struct Node *k : nodes)
    {
        if (k->n == 0)
        {
            z = k;
            continue;
        }

        struct Node *p = k;

        if (k->n > 0)
        {
            for (int i = k->n % (n - 1); i > 0; --i)
                p = p->right;

            if (k == p)
                continue;

            k->right->left = k->left;
            k->left->right = k->right;

            p->right->left = k;
            k->right = p->right;

            p->right = k;
            k->left = p;
        }
        else
        {
            for (int i = k->n % (n - 1); i < 0; ++i)
                p = p->left;

            if (k == p)
                continue;

            k->left->right = k->right;
            k->right->left = k->left;

            p->left->right = k;
            k->left = p->left;

            p->left = k;
            k->right = p;
        }
    }

    int t = 0;

    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 1000; ++j)
            z = z->right;

        t += z->n;
    }

    std::cout << t << std::endl;
}
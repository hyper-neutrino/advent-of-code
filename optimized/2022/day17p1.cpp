#include <iostream>
#include <string>
#include <vector>

std::vector<int> rocks[]{
    {0b0011110},
    {0b0001000, 0b0011100, 0b0001000},
    {0b0011100, 0b0000100, 0b0000100},
    {0b0010000, 0b0010000, 0b0010000, 0b0010000},
    {0b0011000, 0b0011000}};

int main()
{
    std::string s;
    getline(std::cin, s);
    int jl = s.length();

    bool jets[jl];
    for (int i = 0; i < jl; ++i)
        jets[i] = s[i] == '>';

    std::vector<int> tower{0b1111111};
    int height = 0;
    int ri = -1, ji = -1, y;

    for (int rc = 0; rc < 2022; ++rc)
    {
        std::vector<int> rock{rocks[ri = (ri + 1) % 5]};
        y = height + 3;

        while (true)
        {
            if (jets[ji = (ji + 1) % jl])
            {
                for (int i = 0; i < rock.size(); ++i)
                    if ((rock[i] & 1) || (i + y + 1 < tower.size()) && ((rock[i] >> 1) & tower[i + y + 1]))
                        goto end;

                for (int i = 0; i < rock.size(); ++i)
                    rock[i] >>= 1;
            }
            else
            {
                for (int i = 0; i < rock.size(); ++i)
                    if ((rock[i] & 0b1000000) || (i + y + 1 < tower.size()) && ((rock[i] << 1) & tower[i + y + 1]))
                        goto end;

                for (int i = 0; i < rock.size(); ++i)
                    rock[i] <<= 1;
            }

        end:;

            for (int i = 0; i < rock.size(); ++i)
                if ((i + y < tower.size()) && (rock[i] & tower[i + y]))
                    goto end2;

            --y;
            continue;

        end2:

            for (int i = 0; i < rock.size(); ++i)
                if (i + y + 1 < tower.size())
                    tower[i + y + 1] |= rock[i];
                else
                {
                    tower.push_back(rock[i]);
                    ++height;
                }

            break;
        }
    }

    std::cout << height << std::endl;
}
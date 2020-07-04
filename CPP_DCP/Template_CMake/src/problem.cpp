#include "problem.h"

void Solution::make_one(int st, int en, std::string& output)
{
    while(st < en)
    {
        output[st] = 'R';
        output[en] = 'L';
        st++;
        en--;
    }
}

void Solution::pushDominoes(std::string& dominoes)
{
    int start = 0;
    int sz = dominoes.size();

    for (int en = 0; en < sz; en++)
    {
        if (dominoes[en] == 'L')
        {
            if (dominoes[start] = 'R')
                make_one(start, en, dominoes);
            else
            {
                for (int i = start; i < en; i++)
                    dominoes[i] = 'L';
            }
            start = en;
        }
        else if (dominoes[en] == 'R')
        {
            dominoes[en] = 'R';
            start = en;
        }
    }

    if (dominoes[start] == 'R')
    {
        for (; start < sz; start++)
        {
            dominoes[start] = 'R';
        }
    }
}
# Add these to your ~/.bash_aliases

set AOC="~/Desktop/advent-of-code" # remember to change this to whatever your AOC directory is
set AOC_COOKIE="..." # get this from the cookies tab in network tools on the AOC website

alias aos="cd $AOC; python3 solution.py < in.txt"
alias aot="cd $AOC; echo -ne '\\e[0;34m'; python3 solution.py < test.txt; echo -ne '\\e[0m'"
alias aoc="aot; echo; aos"

alias jaos="cd $AOC; bun solution.js in.txt"
alias jaot="cd $AOC; bun solution.js test.txt"
alias jaoc="jaot; echo; jaos"

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" `date +https://adventofcode.com/%Y/day/%d/input` > in.txt
    fi
}
# Advent of Code Guide

Welcome to my Advent of Code guide. In case you don't know what it is, [Advent of Code](https://adventofcode.com/) ("AoC") is a 25-day programming contest where each day, a new problem is released at EST midnight with two parts. Solving each part grants you a star, and the goal is to get all 50 stars. Additionally, the first 100 people to get the right answer get between 1 and 100 points depending on speed, and there is a global leaderboard.

If you are here, you probably already know about this, but if you don't, here are some reasons I would highly recommend participating in the AoC.

1. There is a fantastic community of like-minded people passionate about programming who enjoy challenging themselves, and you will find yourself quickly welcomed even as an absolute beginner with people to help you out and provide resources along the way. Make sure you check out the [official subreddit](https://www.reddit.com/r/adventofcode)!
2. The challenges do not require very difficult concepts, algorithms, or data structures, but are still very good challenges to both your programming skills and problem-solving ability. Unlike many contests that require you to have a repetoire of algorithms, while the AoC does still involve these, it is much more about on-the-spot problem solving and less about being able to recall memorized algorithms.
3. The daily format gives you a good pacing for solving problems. Sometimes, I find that the hardest part about practicing is getting into a routine. It's easy to get a lot of motivation and do a lot in one day (which isn't helpful because you won't learn as efficiently from it, plus you might exhaust your problem set) and then not do enough on other days.
4. If you're interested in the competitive side, the leaderboard is very competitive and it's fun to try to aim for high ranks, either daily or on the global overall leaderboard. If you're not, the challenge is still very enjoyable and you can completely ignore the leaderboard and just challenge your own ability!

# Before we start

Firstly, the leaderboard may not be everyone. You should do the AoC because you find it fun and want to challenge yourself and learn, because you like the community and want to participate in something fun, because you just like coding, etc. If you are motivated because you want to go for leaderboard rankings, go for it! Just don't let the competition get in the way of enjoying the process and learning something out of it. You can also try challenging yourself in ways other than speed - although the leaderboard measures speed, you can try a new language you've been wanting to learn, optimize for speed or resource efficiency, try to find a creative approach, or literally anything else you can think of!

Most importantly, don't let your leaderboard ranking define yourself or your worth as a programmer. Being fast at coding is a good skill, but there are so many skills in coding and no one person is the best at everything. Measuring speed is very linear and involves a lot of factors you may not think about like language choice, computer specs, internet speed, English language comprehension, typing speed, etc.

# The setup

So, you've decided you want to do the AoC, and you'd like to challenge yourself for coding speed. This is what this guide will be about; if you're looking to learn a new language or optimize for efficiency, this is not the right place to go!

You'll want to consider some important factors.

1. **Be available.** This is quite obvious, but you need to be ready at the exact moment the challenge starts. Especially early on, even being a minute late means you will not be on the leaderboard.
2. **Have everything set up.** You should have a text editor or IDE, whatever you are using to run/test your code, and the Advent of Code website window open, plus anything else you might need.
3. **Make sure you won't run into technical issues.** Of course, the unpredictable may happen, but make sure your computer is updated so Windows doesn't decide to update in the middle of you coding, make sure people don't restart or shut off the internet or start downloading something while you're competing, etc.

# Language considerations

My personal recommendation is Python. It has a good amount of important built-ins that you will find helpful, it has low verbosity and overhead and is very fast to write, its performance difference with faster languages like C/C++ does not really matter, and it has some very nice language features that I find repeatedly useful - for example, easy string manipulation, built-in set operations, and infinite integer precision. JavaScript is another good language, as it also has a good amount of useful utilities, and in some situations it may be easier than Python due to the way nested calls are handled (for example, `map(f, map(g, map(h, x)))` in Python requires more nesting and therefore is harder to write than the JavaScript equivalent, `x.map(h).map(g).map(f)`). Additionally, Python lambdas are pretty clunky (`lambda x: x + 1`) as opposed to JS's (`x => x + 1`).

Feel free to use any language you'd like - for optimal leaderboard positions, you definitely want to pick a high level language as opposed to something like C/C++ (for most problems, at least).

Regardless of which language you pick, make sure you have a very solid understanding of the language and know all of its quirks and bonus features that can help you save time. Even if a solution is hacky and involves abusing certain language features, if it's fast to write then that's all you need. Do keep in mind that using AoC to learn a new language can also be very beneficial! Just don't expect good times, but again, that is far from the main reason you should do AoC.

This is Python-specific as that is my language of choice, but the following features are important to know about and/or understand:

- `open(0)` opens STDIN like a file, and you can do `open(0).read()` to get all input or `for line in open(0)` to iterate through lines (the trailing newline is included).
- You can unpack assignment like so: `x, y = input().split()` (if the input line has two things separated by whitespace), instead of `a = input().split()` and then doing `a[0]` and `a[1]`.
- You can create a set from another iterable with `set(...)` or `{ x, y, z, ... }` - sets cannot have duplicates, and if `x` and `y` are sets, then `x & y` is the intersection, `x | y` is the union, `x - y` is the set difference, and `x ^ y` is the symmetric set difference.
- Python has native complex number support, which you can do with `1j`, `-2j`, etc. This is often very helpful for coordinate calculation, since you can just add and subtract them directly which you would not be able to do with pairs. You can also rotate complex coordinates - `x * 1j` rotates counterclockwise 90 degrees, `x * -1j` clockwise by 90 degrees, and `-x` rotates by 180 degrees. Finally, `x.real` and `x.imag` are the real and imaginary components - do note that these are floating-point numbers.
- Understand how to use list slicing - `a[x:y:z]`. You can find a good page on this feature [here](https://www.geeksforgeeks.org/python-list-slicing/). One of the most important ones to know is that `[::-1]` reverses a list or string - `"hello"[::-1] == "olleh"`.

# The meta

Now, let's talk about some things to keep in mind to help you be faster that aren't related to the actual problem-solving component. Firstly, you need to avoid common pitfalls that cause time loss.

## Test your code

Make sure you test your code (unless you are extremely confident). If it takes you 5 seconds to test your code against the sample input (which you can usually copy-paste while reading the actual problem description), then so long as you catch a bug 1 out of 12 times, that is worth it, as the first throttle for an incorrect submission is 1 minute, and it gets even longer if you mess up again. I have the following to assist with this:

- a [userscript](https://github.com/tjjfvi/aoc-2021/blob/main/host/userscript.js) that lets me copy a code-block by right-clicking it, meaning I can easily grab it while reading (made by tjjfvi)
- two separate files `in.txt` and `test.txt` for storing my personal input and the sample input
- a command (`aoc`) that is aliased to run my program on the test output, print it in blue, and then run my program on my real input

With these combined, it only takes me a total of at most 3 seconds to test - I can copy it for basically no time loss, paste it into `test.txt` in about 2 seconds, and then when I run my execution command, I just read the test output and if it's wrong I immediately know I need to fix a bug, and otherwise I can just copy-paste my actual answer, since I ran them at the same time.

You don't need such a setup, but getting into the habit of testing every day means you'll catch these bugs before submitting and won't get hit by the throttle (I didn't do this on 2022 day 1 and lost an easy leaderboard position - the bug was that I saved my file in CRLF mode and not LF mode, which took me only 5 seconds to fix).

## Avoid simple bugs

Obviously, bugs exist because of mistakes, and you can't really just not make mistakes. However, you can change some things to avoid common bugs and mistakes. The first one, ironically, is something that a lot of people run into _because_ they are trying to be fast.

### Variable names

Avoid meaningless variable names. A lot of people just name their variables `a`, `b`, `c`, etc., and then accidentally use the wrong one or overwrite one and their code stops working. It is worth sacrificing a bit of conciseness to avoid painful bugs - these don't always result in errors, you might just be stuck wondering why your calculation looks right but gives the wrong answer for several minutes.

I do still often use single-letter variable names, but if you do, have a convention for it. For me, `a` is my global accumulator array, `t` is my global total (for AoC problems that require you to output a total or count), `i` is reserved for loop index, etc. If you're confident, using single-letter variable names doesn't mean you will necessarily fail, but you have to be careful, and if you can't keep track of all of your variables so well, try using more meaningful names.

Also, avoid using `x` and `y` for 2D arrays. `r` and `c` are generally easier ("row" and "column"), since you will be used to `x` being the horizontal position, whereas `array[x][y]` is the `x`th _row_ and `y`th _column_, which means your coordinates are inverted. Unless you're already used to this and either do `array[y][x]` or just think of `x` as vertical instead, this can lead to a lot of confusion.

Finally, don't use different variable names for the same thing. Keep your naming scheme consistent, and your brain will keep track of them more easily. Establish your own conventions and eventually you will be able to assign and recall your variable names instantly without making mistakes.

### Control flow

It may be tempting to copy-paste a line of code to be faster. This is, indeed, sometimes faster, but if you notice an issue with it, it'll take you more time to change both instances, and that's assuming you remember to change both. If you need to reuse a segment, it's usually better to put it into a function. As with the first tip, this isn't to say that you should never copy-paste code segments, but just be careful and use functions for longer segments especially if you aren't 100% confident that they'll be correct.

### Simplify, and don't optimize where not needed

This may sound obvious, but the simpler your code is, the easier it is to see what's wrong with it and make changes to it. In fact, I often simplify my code to the point of it becoming slightly _less_ efficient, because I'm more confident it will work. If you have a step that you know works but it might be slightly inefficient, it's still probably not slow enough to matter. Moreover, thinking of another method may result in bugs since the more you think, the more likely you are to think about something incorrectly.

That last sentence probably sounds a bit silly, but I've found that just writing the first thing I think of, even if I know there probably exists a smarter way, is better than breaking my train of thought and interrupting my brain from continuing the remainder of the problem. Stopping and breaking my stream of consciousness is not only slower but also may cause my thoughts in the first half and second half to become disconnected and result in bugs from failing the continuation of the problem.

## Catch your bugs early on

Bugs are, as I said, unavoidable, but you should catch them earlier. While solving, try thinking in stages. Let's look at [2022 day 5](https://adventofcode.com/2022/day/5) for example. The first step is to process the first half of the input, so after I did that, I just printed the data and ran it first. If there had been a bug in my input processing, I would have caught it immediately. If you continue with bugs in an earlier part, they become more and more obscure as you go on, and checking in intermediate stages is beneficial. If you have a loop step, it is also not a bad idea to run a print statement in each iteration, check that it looks right, and then comment that out.

In 2022 day 5, I missed a bit in processing my input and had my stacks backwards. This would have potentially been a nuisance to figure out from looking at the incorrect final output, but by just printing it in the middle, I immediately noticed that I needed my stacks to be reversed for the steps I was planning to implement in the second half.

Also, don't remove your test code. Comment it out, so if you do have bugs, you can selectively uncomment them to check the process and intermediate steps.

# Common algorithms, tips, and tricks

Now, let's move on to the actual coding part itself. I will try to be as language-agnostic as possible, but sometimes I will refer to things that may not exist in most languages and are specific to Python.

## Use regex

Sometimes, regular expressions are the easiest way to parse the input. For example, in 2022 day 5, parsing all of the `move # from # to #` could be done by splitting the input and extracting the specific indices 1, 3, and 5. In Python, you can do this with `map(int, input().split()[1::2])`).

However, you can also just find all instances of `/\d+/`; in Python, that would be `import re; map(int, re.findall(r"\d+", input()))`.

Now, in this case, the former is actually shorter and better. However, there are some situations in which regex will be faster, and fitting back into the avoiding bugs theme, you don't have to worry about accidentally indexing incorrectly. Just be careful if the input has floating-point numbers; you might need `/\d+(\.\d+)?/` in that case.

## Don't be afraid to use hacky solutions

For [2022 day 4](https://adventofcode.com/2022/day/4) part 2 (spoiler warning), instead of checking if the intervals overlapped the smart way, I just did `if set(range(a, b + 1)) & set(range(x, y + 1))`. While this is algorithmically slower than the "correct" `if a <= y and b >= x`, the latter would've taken me a bit of time to figure out. Therefore, writing the set intersection saved me time overall. Of course, you might already know how to do interval overlap checking, which would have been a good pattern to have in my memory, but if you run into something like this that you don't already know, don't be afraid to be hacky. Just make sure your code isn't so slow that it doesn't finish in time, and don't go for something too outlandish that might cause you to run into weird bugs.

## Take things step-by-step

Separating your solution into multiple steps has multiple advantages. Firstly, it's easier to debug, as you can check the results in each intermediate step and identify flaws. Secondly, you'll be very likely to find a step that is the same as or very similar to something you've done before, which means you can very quickly know how to solve that component correctly. Finally, if you solve a problem in five steps, you now have five algorithms in your repertoire instead of just the whole problem. This also means that you'll be more likely to find something in the future that you can apply your experience to.

# Practice past problems, and remember interesting tricks

The experience required for solving challenge problems is quite different from that which you gain in regular development. The best way to practice for coding contests is to do coding contest problems. Doing past AoC problems is the best way to familiarize yourself with the style of problems in AoC and some common patterns.

Even if you've solved a problem, try to find a shorter or cleaner solution, or something that is subdivided into more transferable steps. Be sure to check out my solutions (YouTube: https://youtube.com/@hyper-neutrino) to look for any tricks and shortcuts, as well as solutions from other top-ranking users. On the leaderboard, if a user's name is green, they've linked their GitHub account and you can click it to go to their GitHub profile. One person's I would 100% recommend is [betaveros](https://github.com/betaveros). He has been #1 on the 2021, 2020, and 2019 leaderboards, as well as #2 in 2018, and there are a lot of tactics to learn from him.

---

# Conclusion

I've given you some meta tips and advice, but ultimately, experience and pattern recognition are two of the most important parts of problem solving in the context of these coding challenges, and I cannot teach those. Practice is the best way to improve at anything, and hopefully my tips on how to practice effectively and how to approach these types of problems will help you throughout the learning process.
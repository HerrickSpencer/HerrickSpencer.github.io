---
layout: WPArchive
title: The Sudoku Solver&hellip;. Episode one
date: 2011-10-19 19:17
author: herrickspencer
comments: true
categories: [Programming]
---
I’ve been doing some interviewing for open positions at Microsoft… and one of the portions of any MS interview is usually a coding question to gauge the level of algorithm maturity of the candidate…  not necessarily the mastery of syntax or knowledge of the CLR, but simply how you think through solving a problem.

One of my code questions was: “Say you are part of a project for writing a Sudoku game, and your part is to verify if the user has correctly solved the puzzle. Given an array representing the 9x9 grid for the Sudoku possible answer; Write a function that returns a bool to determine if an answer is correct. ”   This has resulted in several interesting paths of thought on the part of the candidates, but also sparked some interesting discussions in house as well.

[![The previous puzzle, solved with additional numbers that each fill a blank space.](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)](https://en.wikipedia.org/wiki/Sudoku){: .left}
If you don’t know about Sudoku, it is a simple game, consisting of a 9x9 grid where the object is to get numbers 1 through 9 into each square, with no duplicates in a column, or a row, or a 3x3 box.

(picture is from [Wikipedia](https://en.wikipedia.org/wiki/Sudoku) entry)

The problem is interesting because it is simple in verifying columns and rows, but holds a hidden problem when trying to do the same for the ‘boxes’.

In particular, Kevin Johnson and I were coming up with possible multi-threaded approaches to solving the problem.  We even expanded this issue to include **solving** the puzzle rather than just verifying.  This is because I’d completed this (to an extent) in Perl some years back.  But first… let’s discuss the puzzle verification function.

The most common answers to the verification steps involve two nested for loops to iterate through the cells. On each cell you’d store or check off that number from a global (to the loops) sets of objects, either numbers or Boolean to keep a check list of what you’ve encountered already in that column/row/box.   Sometimes people don’t really think about the boxes till they’ve completed the column/row check, and that’s where things get a bit hairy…

One Common Interview Answer:

```C#
bool isSudokuSolved(Int[,] solution)
{
    HashSet<Int>[] rows = new HashSet<Int>[9];
    // ignoring initializing rows hash...
    //  ignoring test code (verify array size, numbers are 1-9 etc...)

    for (int x = 0; x < 9; x++)
    {
            // initialize cols hash
        HashSet<Int> cols = new HashSet<Int>();
        
        for (int y = 0; y < 9; y++)
        {
                //initialize row hash
                if (x==0){         
                    rows[y] = new HashSet<Int>();
                }

            //Check rows and cols by add new (which returns bool for !existance)
            if (
                (!cols.Add(solution[x, y]))
                || (!rows[y].Add(solution[x, y]))
                )
            {
                return false; //dupe
            }
            
            //check for box duplicates
            if (x % 3 == 0 && y % 3 == 0)
            {
                //It's the top left corner of a box
                if (!CheckBox(solution, x, y))
                {
                    return false;
                }
            }
        }
    }
    return true;
}

bool CheckBox(short[,] solution, int X, int Y)
{
    HashSet<Int> box = new HashSet<Int>();
    for (int x = X; x < X+3; x++)
    {
        for (int y = Y; y < Y+3; y++)
        {
            if (!box.Add(solution[x, y]))
            {
                return false; //dupe
            }
        }
    }
    return true;
}
```

In addition to this, there were concepts of keeping a bit array that will be pre-populated to keep track of all the answers that have already been found, returning false on any that are already set to true.  This though is very similar to the above example, though it uses more data (potentially on an early exit example), but may (debatable) use less process time since it is not using a hashset.

Next I’ll try to add on to this as to thoughts of what the “Solver” should look like, possible answers being pursued… etc.   If you have your own answer for the above… feel free to post it in the comments.

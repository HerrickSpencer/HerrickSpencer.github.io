---
layout: post
title: The Sudoku Solver&hellip;. Episode one
date: 2011-10-19 19:17
author: herrickspencer
comments: true
categories: [Programming]
---
<p>I’ve been doing some interviewing for open positions at Microsoft… and one of the portions of any MS interview is usually a coding question to gauge the level of algorithm maturity of the candidate…&nbsp; not necessarily the mastery of syntax or knowledge of the CLR, but simply how you think through solving a problem. </p> <p>One of my code questions was: “Say you are part of a project for writing a Sudoku game, and your part is to verify if the user has correctly solved the puzzle. Given an array representing the 9x9 grid for the Sudoku possible answer; Write a function that returns a bool to determine if an answer is correct. ”&nbsp;&nbsp; This has resulted in several interesting paths of thought on the part of the candidates, but also sparked some interesting discussions in house as well.</p> <p><a href="http://en.wikipedia.org/wiki/Sudoku"><img style="display:inline;float:right;margin:0 0 0 5px;" alt="The previous puzzle, solved with additional numbers that each fill a blank space." align="right" src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png" width="250" height="250"></a>If you don’t know about Sudoku, it is a simple game, consisting of a 9x9 grid where the object is to get numbers 1 through 9 into each square, with no duplicates in a column, or a row, or a 3x3 box.</p> <p>(picture is from <a href="http://en.wikipedia.org/wiki/Sudoku" target="_blank">Wikipedia</a> entry)</p> <p>The problem is interesting because it is simple in verifying columns and rows, but holds a hidden problem when trying to do the same for the ‘boxes’.</p> <p>In particular, Kevin Johnson and I were coming up with possible multi-threaded approaches to solving the problem.&nbsp; We even expanded this issue to include <strong>solving </strong>the puzzle rather than just verifying.&nbsp; This is because I’d completed this (to an extent) in Perl some years back.&nbsp; But first… let’s discuss the puzzle verification function.</p> <p>The most common answers to the verification steps involve two nested for loops to iterate through the cells. On each cell you’d store or check off that number from a global (to the loops) sets of objects, either numbers or Boolean to keep a check list of what you’ve encountered already in that column/row/box.&nbsp;&nbsp; Sometimes people don’t really think about the boxes till they’ve completed the column/row check, and that’s where things get a bit hairy…</p> <p>One Common Interview Answer:</p><pre class="csharpcode"><span class="kwrd">bool</span> isSudokuSolved(Int[,] solution)
{
    HashSet&lt;Int&gt;[] rows = <span class="kwrd">new</span> HashSet&lt;Int&gt;[9];
    <span class="rem">// ignoring initializing rows hash...</span>
    <span class="rem">//  ignoring test code (verify array size, numbers are 1-9 etc...)</span>

    <span class="kwrd">for</span> (<span class="kwrd">int</span> x = 0; x &lt; 9; x++)
    {
            <span class="rem">// initialize cols hash</span>
        HashSet&lt;Int&gt; cols = <span class="kwrd">new</span> HashSet&lt;Int&gt;();
        
        <span class="kwrd">for</span> (<span class="kwrd">int</span> y = 0; y &lt; 9; y++)
        {
                <span class="rem">//initialize row hash</span>
                <span class="kwrd">if</span> (x==0){         
                    rows[y] = <span class="kwrd">new</span> HashSet&lt;Int&gt;();
                }

            <span class="rem">//Check rows and cols by add new (which returns bool for !existance)</span>
            <span class="kwrd">if</span> (
                (!cols.Add(solution[x, y]))
                || (!rows[y].Add(solution[x, y]))
                )
            {
                <span class="kwrd">return</span> <span class="kwrd">false</span>; <span class="rem">//dupe</span>
            }
            
            <span class="rem">//check for box duplicates</span>
            <span class="kwrd">if</span> (x % 3 == 0 &amp;&amp; y % 3 == 0)
            {
                <span class="rem">//It's the top left corner of a box</span>
                <span class="kwrd">if</span> (!CheckBox(solution, x, y))
                {
                    <span class="kwrd">return</span> <span class="kwrd">false</span>;
                }
            }
        }
    }
    <span class="kwrd">return</span> <span class="kwrd">true</span>;
}

<span class="kwrd">bool</span> CheckBox(<span class="kwrd">short</span>[,] solution, <span class="kwrd">int</span> X, <span class="kwrd">int</span> Y)
{

    HashSet&lt;Int&gt; box = <span class="kwrd">new</span> HashSet&lt;Int&gt;();
    <span class="kwrd">for</span> (<span class="kwrd">int</span> x = X; x &lt; X+3; x++)
    {
        <span class="kwrd">for</span> (<span class="kwrd">int</span> y = Y; y &lt; Y+3; y++)
        {
            <span class="kwrd">if</span> (!box.Add(solution[x, y]))
            {
                <span class="kwrd">return</span> <span class="kwrd">false</span>; <span class="rem">//dupe</span>
            }
        }
    }
    <span class="kwrd">return</span> <span class="kwrd">true</span>;
}</pre>
<p>&nbsp;</p>
<p>In addition to this, there were concepts of keeping a bit array that will be prepopulated to keep track of all the answers that have already been found, returning false on any that are already set to true.&nbsp; This though is very similar to the above example, though it uses more data (potentially on an early exit example), but may (debatable) use less process time since it is not using a hashset.</p>
<p>Next I’ll try to add on to this as to thoughts of what the “Solver” should look like, possible answers being pursued… etc.&nbsp;&nbsp; If you have your own answer for the above… feel free to post it in the comments.</p>

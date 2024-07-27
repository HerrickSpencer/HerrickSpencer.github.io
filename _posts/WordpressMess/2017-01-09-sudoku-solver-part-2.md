---
layout: WPArchive
title: Sudoku Solver&ndash;Part 2
date: 2017-01-09 00:52
author: herrickspencer
comments: true
categories: [Programming, Sudoku, Technology]
---
I have recently had the opportunity to pose the [original Sudoku question]({% post_url 2011-10-19-the-sudoku-solver-episode-one %}) to some tech questions to some colleagues and geeky visitors at my office. It inspired me to make an update to that blog post, and also to upload the code I’d worked on back in 2011 that solved these puzzles in an interesting way.</p>

If you don’t recall, the [original Sudoku question](/_posts/the-sudoku-solver-episode-one) was to code a simple function that would return a value indicating if a Sudoku puzzle given as input was correctly solved. I’d posted an example of one common solution in C# (based on answers I was given) and got many responses to this problem. In this round I’d like to add some additional methods of solving the problem, as well as introduce the code I’d worked on 6 yrs ago that would self solve a puzzle as the puzzle was input into the program, simply by driving solving logic using event handling only.

<h2>My 6yr old Event Based solver</h2>

<a href="/{{ site.postMedia }}/2017/01/sudokusolver-v1-ui.jpg"><img title="SudokuSolver v1 UI" style="background-image:none;float:left;padding-top:0;padding-left:0;margin:0 6px 0 0;display:inline;padding-right:0;border-width:0;" border="0" alt="SudokuSolver v1 UI" src="/{{ site.postMedia }}/2017/01/sudokusolver-v1-ui_thumb.jpg" width="184" align="left" height="244" /></a>I’ve uploaded to <a href="https://github.com/HerrickSpencerMSFT">GitHub[tbd]</a> and <a href="https://bitbucket.org/byterisc/sodokusolver_eventdriven">BitBucket</a> my 2011 solution, and plan to update this to use UWP as the UI (to put it in the store), as well as the new Inking feature to enter the numbers by pen/touch.

<h2>Quick summary</h2>

<ul>   <li>Written (ca. October 2011) originally as a conversion of a Perl program to C#, this is a Sudoku solver that primarily works using events triggered by changes to the grid. It 'self solves' as any cell is entered or solved for asynchronously. </li> </ul>

<h2>Longer description:</h2>

This started as a Perl program I wrote (included in the repo) that I used to help solve difficult Sudoku puzzles... then I tried to use that perl code to solve the most difficult ones and it works well. However, I wanted to study async programming and eventing in C#... so I decided to rewrite the project in C# as a library for a console app. (The Console app is still included in the project) This is where the project turned into a purely event driven program. Only when a cell is changed, either by the user or the solver itself, will the solver run any logic to solve additional cells. It uses a hierarchy of inherited classes to accomplish this, each doing work for their respective type. It works only by events thrown when any cell is either changed or solved. This in turn 'tells' the related cells in columns, rows, or boxes to attempt to solve themselves. 

The UI also has some controls to allow for loading puzzles from text files for testing (see the root Boards directory) and for loading the file that contains &quot;the hardest Sudoku puzzle&quot;<sup>1</sup>. It also has the ability to save a puzzle to a text tile for use in the program. This is very useful for creating unit tests as well as it is the format the solver library can import. 

The last function of the UI is a TryBreak button that will attempt to forcibly solve the puzzle by brute force. This is done by cycling through each cell attempting a possible value till the correct one is found. 

<em>(1) = I can not verify the validity of this being the hardest puzzle... I've seen multiple claiming to be the most difficult.</em>

<h2>Interesting Solutions offered by Colleagues/Visitors</h2>

<h6>Ground rules: </h6>

These sulutions do not solve, but they are simply the function that verifies if a solution is valid.    <br />“Say you are part of a project for writing a Sudoku game, and your part is to verify if the user has correctly solved the puzzle. Given an array representing the 9×9 grid for the Sudoku possible answer; Write a function that returns a bool to determine if an answer is correct. ”&#160; 

<h4>Sum and Product:</h4>

One of the two interesting solutions was reminded to me by my manager (and coincidentally thought of in the same day by his manager!) is one I’d seen a long while back while interviewing in NY. This solution involves the idea that given a set (column, row, or box); if you take each number in that set and add them together, you should get 45. Then take each number in that set and multiply them all together, you should get 362880.&#160; By testing each column, row, and grid in this way, you will verify the solution.&#160; Very nice solution. 

See if you can code this up with as minimal for loops as possible, or even better, use Linq to simplify the logic! I might just post the solutions if you do… <img class="wlEmoticon wlEmoticon-smile" style="border-style:none;" alt="Smile" src="/{{ site.postMedia }}/2017/01/wlemoticon-smile.png" />

<h4>Bit&lt;&lt;Shift Checker</h4>

This is a solution I saw just one time, and I liked the idea… the original coder did this in C++, which is a more elegant way to accomplish this, but I’ve coded up a version of it in C# for you (and to allow you to figure out the C++ version yourself <img class="wlEmoticon wlEmoticon-smile" style="border-style:none;" alt="Smile" src="/{{ site.postMedia }}/2017/01/wlemoticon-smile.png" /> )&#160;&#160; There are many ways this code can be improved… and made less readable <img class="wlEmoticon wlEmoticon-winkingsmile" style="border-style:none;" alt="Winking smile" src="/{{ site.postMedia }}/2017/01/wlemoticon-winkingsmile.png" /> but I left that for you to comment on too.&#160; The general idea is to use a bit for each number 1-9, and as you see it flip it up. This is done by bitshifting a 1 to the number found… example if a 5 is found, 1&lt;&lt;5 = 00000100000. As you hit each number, you will OR against it to either set it to 1. If the number is not seen at all, the answer will not be all 1111111110. Even dupes are handled this way as one dupe would mean that another number will be missing.

&#160;

<pre>static bool ValidateSodokuBitShiftVer(int[,] answer)
{
    // 1022 is equivalent to (Convert.ToInt16(&quot;1111111110&quot;, 2)); //zero accounts for a 1 based number set
    int fullset = 1022; 
    var Rows = new int[9];
    var Cols = new int[9];
    var Boxes = new int[9];

    for (int row = 0; row &lt; 9; row++)
    {
        for (int col = 0; col &lt; 9; col++)
        {
            var answerItem = 1 &lt;&lt; answer[row, col];
            var boxNumber = col / 3 + (row / 3) * 3;

            Rows[row] |= answerItem;
            Cols[col] |= answerItem;
            Boxes[boxNumber] |= answerItem;
        }
    }

    return !(
        Rows.Any((x) =&gt; x != fullset)
            |
        Cols.Any((x) =&gt; x != fullset)
            |
        Boxes.Any((x) =&gt; x != fullset)
        );
}</pre>

&#160;

<h2>Comments welcome!</h2>

Can you code the C++ version of this? or make improvements? to any of the solutions above?

Send me comments below!

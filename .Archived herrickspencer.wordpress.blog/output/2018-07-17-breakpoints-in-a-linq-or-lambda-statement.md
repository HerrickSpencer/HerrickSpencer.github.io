---
layout: post
title: TOW-Breakpoints in a LINQ or Lambda statement
date: 2018-07-17 18:00
author: herrickspencer
comments: true
categories: [Breakpoints, C#, debugging, Lambda, LINQ, Programming, Tip Of The Week, Visual Studio]
---
<img src="https://herrickspencer.blog/wp-content/uploads/2012/10/clip_image0011.jpg" />

In the most recent update of Visual Studio, one of the new features is the ability to convert a LINQ query to a foreach statement. When this was pointed out to me in an email, I jokingly responded, “Why would you want to do that!?”, because I favor Lambda and LINQ statements over for/foreach.

My co-worker replied that one of the reasons someone may want to do this is to ease debugging since it is difficult to set a breakpoint on the meat of the statement and not the whole lambda itself.  This issue leaves one to believe you can’t debug something run inside a lambda, but only the instantiation of the lambda/LINQ item itself, due to delayed execution; usually delayed until you are ready to use the items returned. This leads to ‘jumping over’ the execution of the LINQ query, leading some to believe you can’t actually break on each item in an array/list.

The <a href="https://msdn.microsoft.com/en-us/library/5557y8b4.aspx">Microsoft Docs page for breakpoints</a> doesn’t even elude to how to remedy this issue.

Yet…. there is a way to do this easily! VS has included this since around VS 2013.  Let’s dive into some small code and check it out.

<pre>1            List strs = new List{ "this", "that", "then" };
2            var temp = strs.Where(x =&gt; x.StartsWith("the"));
3            var temp2 = from str in strs where str.StartsWith("the") select str;
4            temp.ToList().ForEach(x =&gt; Console.WriteLine(x));
5            temp2.ToList().ForEach(x =&gt; Console.WriteLine(x));
</pre>

so in the two examples of inline lambda and LINQ on lines 2 and 3, it is common for a developer to feel that a breakpoint on these lines will do nothing, since it just steps over the instantiation of the query, and the delayed execution they really want to break on is done later on lines 4 and 5. It may seem infuriating that you seem not to be able to break on the actual loop for each member of the array “strs” involved in the StartsWith method.

Well, you can do this easily!  Just place the cursor on the StartsWith prior to hitting F9 to add a breakpoint at that point. It will indicate that this section of the line will be the breakpoint by highlighting just the x.StartsWith('the”) portion of that line. It will now hit that code each time as it enumerates through the array.

<a href="http://herrickspencer.blog/wp-content/uploads/2018/07/image.png"><img style="display:inline;background-image:none;" title="image" src="http://herrickspencer.blog/wp-content/uploads/2018/07/image_thumb.png" alt="image" width="642" height="132" border="0" /></a>

I’m sure that there are MANY of you who know about this, and likely have known for years… but it is my experience that there are just as many whom have never seen this and have been frustrated with this ‘inability of Visual Studio’ that are now happy to find the answer.

Cheers, and happy coding!

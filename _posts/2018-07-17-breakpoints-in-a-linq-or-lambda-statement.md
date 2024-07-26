---
layout: post
title: TOW-Breakpoints in a LINQ or Lambda statement
date: 2018-07-17 18:00
author: herrickspencer
categories:
- Tip Of The Week
- Programming
tags:
- Breakpoints
- C#
- Visual Studio
- Debugging
- Lambda
- LINQ
- Tip Of The Week
- Visual Studio
---
![TOW](/{{ site.postMedia }}/TipOfTheWeek.jpg)

In the most recent update of Visual Studio, one of the new features is the ability to convert a LINQ query to a `foreach` statement. When this was pointed out to me in an email, I jokingly responded, “Why would you want to do that!?” because I favor Lambda and LINQ statements over `for`/`foreach`.

My co-worker replied that one of the reasons someone may want to do this is to ease debugging. It is difficult to set a breakpoint on the meat of the statement and not the whole lambda itself. This issue leaves one to believe you can’t debug something run inside a lambda, but only the instantiation of the lambda/LINQ item itself, due to delayed execution (usually delayed until you are ready to use the items returned). This leads to ‘jumping over’ the execution of the LINQ query, leading some to believe you can’t actually break on each item in an array/list.

The [Microsoft Docs page for breakpoints](https://msdn.microsoft.com/en-us/library/5557y8b4.aspx) doesn’t even elude to how to remedy this issue.

Yet… there is a way to do this easily! Visual Studio has included this since around VS 2013. Let’s dive into some small code and check it out:

```csharp
List<string> strs = new List<string> { "this", "that", "then" };
var temp = strs.Where(x => x.StartsWith("the"));
var temp2 = from str in strs where str.StartsWith("the") select str;
temp.ToList().ForEach(x => Console.WriteLine(x));
temp2.ToList().ForEach(x => Console.WriteLine(x));
```

In the two examples of inline lambda and LINQ on lines 2 and 3, it is common for a developer to feel that a breakpoint on these lines will do nothing, since it just steps over the instantiation of the query. The delayed execution they really want to break on is done later on lines 4 and 5. It may seem infuriating that you seem not to be able to break on the actual loop for each member of the array “strs” involved in the `StartsWith` method.

Well, you can do this easily! Just place the cursor on the `StartsWith` prior to hitting F9 to add a breakpoint at that point. It will indicate that this section of the line will be the breakpoint by highlighting just the `x.StartsWith("the")` portion of that line. It will now hit that code each time as it enumerates through the array.

![Debugging](/{{ site.postMedia }}/2018/07/image_thumb.png)

I’m sure that there are MANY of you who know about this, and likely have known for years… but it is my experience that there are just as many who have never seen this and have been frustrated with this ‘inability of Visual Studio’ that are now happy to find the answer.

Cheers, and happy coding!
---
layout: post
title: TOW&ndash;C# Pattern matching-syntactic sugar
date: 2018-02-26 10:42
author: herrickspencer
comments: true
categories: [C# Pattern matching, Programming, Tip Of The Week]
---
<img src="https://herrickspencer.blog/wp-content/uploads/2012/10/clip_image0012.jpg" />

I always forget this is available… but IntelliSense reminded me, so I thought I’d point out this jewel.

<a href="https://docs.microsoft.com/en-us/dotnet/csharp/pattern-matching" target="_blank" rel="noopener">Pattern matching from Docs</a>:

<blockquote>Patterns test that a value has a certain shape, and can extract information from the value when it has the matching shape. Pattern matching provides more concise syntax for algorithms you already use today. You already create pattern matching algorithms using existing syntax. You write if or switch statements that test values. Then, when those statements match, you extract and use information from that value. The new syntax elements are extensions to statements you are already familiar with: is and switch. These new extensions combine testing a value and extracting that information.</blockquote>

<h6>IS type pattern works like this…</h6>

If you have this code normally:

<pre>MyType possibleMyType = item as MyType;
if (possibleMyType != null)
{ //do something }</pre>

Rewrite with pattern matching… as

&nbsp;

<pre>if (item is MyType possibleMyType)
         { // do something better using possibleMyType as a new variable }</pre>

<h6></h6>

<h6>A switch case statement can be written like so:</h6>

<pre>object possibleMyType = ReturnAnObject(Foo);
switch(possibleMyType)
{
    case MyType myTypeValue when myTypeValue.myProp = 3:
          // Do something better when type and a property value matches your target
          break;
    case MyType myTypeValue:
          // Do something when a type matches your target
          break;
    case NotMyType notMyTypeValue:
          // Do something different
          break;
    case null:
          throw new ArgumentNullException(“OOPS! I’m Null!”);
    default:
          throw new ArgumantException(
                message: “Failed type matching”,
                paramName: nameof(possibleMyType));
 }
</pre>

And there is a few more cases in the doc… like using var in the switch to do some complex matching. go check it out!

Cheers!

---
layout: post
title: 'TOW: Visual Studio Solution Search case sensitivity'
categories:
- Tip Of The Week
- Programming
tags:
- Tip Of The Week
- Programming
- Visual Studio
- File Search
excerpt: Case sensitivity rules in the solution search, OCR gets nothing... Ocr will.
  and so will ocr, because that last one is case-insensitive. Read to learn the rules!
date: 2024-10-05 14:36 -0700
image: /assets/img/postMedia/VisualStudioSolutionFileNotFound.png
---

Case sensitivity rules in the solution search are a bit interesting, and can be frustrating if you don't understand the rules, and helpful when you do.

## Table of Contents <!-- omit in toc -->
- [Backstory](#backstory)
- [It works on my machine (Closed: as designed)](#it-works-on-my-machine-closed-as-designed)
- [An easier way: Code Search](#an-easier-way-code-search)


## Backstory

In a large project I was working in I used ctrl+; to get to the solution search bar to find and select a file I needed to edit. I didn't really remember the  file's name, so I made a guess that it was something that contained 'OCR' and 'Provider'. I entered 'OCRProvider' to make a guess. To my surprise, nothing was returned. How was this possible? I knew for a fact there were several files that had this string. So I widened the search to just 'OCR'... and was shocked to find that, again, nothing was found!  At this point, I decided there was a bug in the search feature in Visual Studio, so I started testing.

I discovered that the string was acting case-sensitively. This seemed fine, but not ideal to me for users. If I put my search string in perfectly the way the file had it "OcrProvider" (PascalCase) then it would be found. If I entered it all lowercase "ocrprovider" it would also be found. So I went to file a bug with the feedback tool. 

## It works on my machine (Closed: as designed)

However I discovered that this was as expected!

OCR gets nothing... however Ocr will. and so will ocr, because that last one is case-insensitive.

Answer from "Solution Explorer search case sensitive - Developer Community (visualstudio.com)"

>Thank you very much for sharing your feedback! The current Solution Search behavior is complex, but the result in this case is still as intended.
>
>Solution Explorer is built with a provider model - solutions, projects, files are provided by Hierarchy Provider; classes, methods, properties are provided by File Content Provider. When a search is done, it is up to the provider to interpret the query and unfortunately the providers have different behaviors.
>
> Hierarchy Provider: For each item, the search will be done against the item name
>
> If the search term does not have any upper case characters, do a case-insensitive match.
If the search term contains one or more upper case characters, do a case-sensitive match.
>
> If the search term contains all upper case characters, do a camel case match if the case-sensitive match returns no result.
>
>File Content Provider: Search results can vary depends on the programming language (each language can provide its own File Content Provider). But in your scenario, C# language seems to perform camel case match as a fall back always. This behavior can be verified by typing <Ctrl+,> to launch Go to search, then search for DFU.
>
> So in this case, Solution Explorer is showing the camel case search result from File Content Provider. If you intend to search in file name only, please consider turning off ‘Search within file contents’ (drop down on the right of Solution Explorer search box), which will restrict to the Hierarchy Provider behavior. Unfortunately this will still result in camel case match for all-upper-case terms, but the result set will be on file name only.

## An easier way: Code Search

I'd recommend always using lowercase in the Solution Search bar, but if you need a much better search experience, use the Code Search feature by shortcut `Ctrl+T` or `Ctrl+`, Then enter a file name search using the prefix `f:` as in `f:OCRProvider`.

In fact, this code search window is also far more effective when trying to do reference searches, find results etc.  I would not go back to using the "Find All References" view since I've used this window, try it out!

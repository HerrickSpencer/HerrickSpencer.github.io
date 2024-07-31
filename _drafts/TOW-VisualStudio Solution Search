---
layout: post
title: 'TOW: Visual Studio Solution Search case sensitivity'
categories:
  - Tip Of The Week
  - Programming
  - Visual Studio
tags:
  - Tip Of The Week
  - Programming
  - Visual Studio
  - File Search
excerpt: Case sensitivity rules in the solution search, OCR gets nothing... Ocr will. and so will ocr, because that last one is case-insensitive. Read to learn the rules!
---

Case sensitivity rules in the solution search:
OCR gets nothing... Ocr will. and so will ocr, because that last one is case-insensitive.

Solution Explorer search case sensitive - Developer Community (visualstudio.com)

Thank you very much for sharing your feedback! The current Solution Search behavior is complex, but the result in this case is still as intended.
Solution Explorer is built with a provider model - solutions, projects, files are provided by Hierarchy Provider; classes, methods, properties are provided by File Content Provider. When a search is done, it is up to the provider to interpret the query and unfortunately the providers have different behaviors.

    Hierarchy Provider: For each item, the search will be done against the item name

    If the search term does not have any upper case characters, do a case-insensitive match.
    If the search term contains one or more upper case characters, do a case-sensitive match.

    If the search term contains all upper case characters, do a camel case match if the case-sensitive match returns no result.

    File Content Provider: Search results can vary depends on the programming language (each language can provide its own File Content Provider). But in your scenario, C# language seems to perform camel case match as a fall back always. This behavior can be verified by typing <Ctrl+,> to launch Go to search, then search for DFU.
    So in this case, Solution Explorer is showing the camel case search result from File Content Provider. If you intend to search in file name only, please consider turning off ‘Search within file contents’ (drop down on the right of Solution Explorer search box), which will restrict to the Hierarchy Provider behavior. Unfortunately this will still result in camel case match for all-upper-case terms, but the result set will be on file name only.


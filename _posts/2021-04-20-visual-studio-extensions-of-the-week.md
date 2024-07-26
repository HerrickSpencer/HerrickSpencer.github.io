---
layout: post
title: Visual Studio extensions of the week
date: 2021-04-20 15:48
author: herrickspencer
comments: true
categories:
- Programming
- Tip Of The Week
tags: [Programming, Visual Studio, Tip Of The Week]
---
I recently found two extensions to Visual Studio that I have been using for a week or more and don’t know how I could have done without them. I thought it best to add a quick post to both tell any poor soul visiting this long forgotten blog site about them; as well as to make a way for me to remember them if I forget which ones these are in the future.

Here they are in no particular order.

[ResX Resource Manager](https://github.com/dotnet/ResXResourceManager) is a way to view all your resource strings across all projects in the solution in the same place. Also has some very nice ways to search and filter for items.

![VisualStudioMainScreen.png](https://github.com/dotnet/ResXResourceManager/blob/master/Assets/VisualStudioMainScreen.png?raw=true)

[Favorite Documents](https://vlasovstudio.com/favorite-documents/) is also a great extension for making a list (per solution or for all solutions) that will link to documents you open frequently, but are a bit cumbersome due to folder structure to get to. Yeah, I know you can just ctrl+; to search the files in your solution… but you may have several match that text and still need to hunt to find the correct one. Leave me alone, I like this extension.

![Favorites menu in Visual Studio 2010](https://vlasovstudio.com/favorite-documents/favorites-menu-in-visual-studio-2010.png)

[Serialize This](https://github.com/CodeCasterNL/CodeCaster.SerializeThis/blob/master/README.md) is the last one, and I like it for being able to quickly get a JSON format of a class I’d like to create a sample data document from, mostly for testing or debugging purposes. You can right-click on a type in your code, create the JSON file then deserialize that file back into the project for the use of a mock datasource or other purpose.
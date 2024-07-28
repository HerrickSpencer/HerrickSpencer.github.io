---
layout: WPArchive
title: Visual Studio &ndash; Reference hopping, code snippets, and other handy shortcuts
date: 2012-10-23 15:54
author: herrickspencer
comments: true
categories: [Programming, Tip Of The Week]
tags: [Visual Studio, Tip Of The Week]
---
Again, I’m posting another Visual Studio tip… this one is something I bet you have had experience with one or the other…

![Tip of the Week]({{ site.postMedia}}/TipOfTheWeek.jpg)

## Reference hopping

When first using VS2010, I was glad to see that when I had the cursor on a variable name, class name, property name etc, it would highlight every other reference to that item in the document I was viewing. However, I missed the essential feature that corresponds to that highlighting. Reference hopping, (until I discover what the real name is, that’s what I’m calling it…) when you press Ctrl+Down/Up Arrow, the cursor jumps to the next reference to that item in your document, in the direction you specified, it also will wrap around when no more references are found in that direction.

[![clip_image001](/{{ site.postMedia }}/2012/10/clip_image001.png "clip_image001")](https://my/sites/herricks/TipOfTheWeek/Lists/Posts/Attachments/13/clip_image002_2_14C01B2F.png)

## Code Snippets

The next item I never see anyone use, but is clearly useful is code snippets. For example when writing a standard for loop, you might not want to have to type every step… try just typing “for” then hit Tab. VS will fill in the entire For loop, highlighting the iteration variable:

[![clip_image001[5]](/{{ site.postMedia }}/2012/10/clip_image0015.png "clip_image001[5]")](https://my/sites/herricks/TipOfTheWeek/Lists/Posts/Attachments/13/clip_image003_2_14C01B2F.png)

By typing a new name for the “i” then hitting Tab again, it will update the rest of the “i” variables with the name you give… very handy.

[![clip_image001[11]](/{{ site.postMedia }}/2012/10/clip_image00111.png "clip_image001[11]")](https://my/sites/herricks/TipOfTheWeek/Lists/Posts/Attachments/13/clip_image004_2_14C01B2F.png)

## Some other really helpful items:

| **Keyboard shortcut** | **Resulting action** |
| --- | --- |
| **Shift+F12** | List references of item under cursor |
| **Ctrl+\]** | While on a scope enclosure: brace or bracket {,}, (, or ) will bring you to the matching brace. |
| **Ctrl+space** | Complete the item under the cursor or bring up completion dialog |
| **Ctrl+shift+space** | Show the param info for the method under cursor |
| **Ctrl+K,I** | Shows the definition for the item under the cursor |
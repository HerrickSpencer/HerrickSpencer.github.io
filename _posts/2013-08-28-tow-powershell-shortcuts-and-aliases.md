---
layout: WPArchive
title: TOW &ndash; PowerShell Shortcuts and Aliases
date: 2013-08-28 10:23
author: herrickspencer
comments: true
categories: [Programming, Tip Of The Week]
tags: [PowerShell, Tip Of The Week]
---
![Tip-of-the-week]({{ site.postMedia }}/TipOfTheWeek.jpg)

I love scripting, Perl, PowerShell, SQL, whatever is most convenient to get the job done with minimal effort… and allow me to record my script to use when the issue presents itself in the future. One of the things that coders love to do is make something that is already convenient, even MORE convenient.

Let's take Aliases… this is not a new concept. In DOS shell, 'CD' is actually an Alias for 'CHDIR'…. Someone just thought they could increase productivity of command entry by reduce their command entry time by 60%! It is so hard to enter those middle three letters… let's get rid of them. 

(Reminds me of Simpsons &quot;King Size Homer&quot; where he learns pressing 'Y' is the same as entering 'YES', thus he exclaims he has tripled his productivity)

Quick note you may not know; to make current drive switch too when CD'ng to a path not on current drive letter, Use &quot;CD /D [path]&quot; 

## PS Aliases

First look up aliases in PS, nice quick way to shorten your keyboard time… Get-Alias [command you want shortcut for] 

```PowerShell
Example: Set-Content = SC
```

## Where Alias

You get a slew of data back from a command (&quot;Get-ChildItem&quot; for example to get files at current directory) but want to filter this list to only the interesting items. So you pipe this into Where-Object

```PowerShell
Get-ChildItem | Where-Object –Property "Name" –Value "myfile.txt" –EQ
```

However, this is long, messy, and doesn't allow for us to 'get creative'… let's try it with the alias for Where-Object, the ? symbol:

```PowerShell
GCI | ?{$\_.Name –eq "myfile.txt"}
```

WoW, we saved 36 keystrokes, over half of the original command! Let's dig in a bit… the ? obviously replaces the Where-Object command… then we've replaced the normal properties with the filter script enclosed in brackets. We also used a default variable $\_ used in PS and Perl to denote the object being acted on in the enumerative filtering going on.

### ForEach-Object Alias

Next let's check out the next most likely thing to do to a return list, iterate an action on the items with For-Each. First, the alias for ForEach-Object is simply foreach, but we can do even better than that, by using the % symbol alias. In a sense, the \| pipe is a foreach, passing the results of one command directly into the next. However, there are situations where you want to do multiple things at a time on a result object. Let's try tanking our last command, and copy the txt files to another folder, simultaneously counting the number of files we copy that are over 2MB in size at the same time.

```PowerShell
$newPath = \[choose path to copy to\];

GCI | ?{$\_.Name –like "\*.txt"} | ForEach { if ( ($\_.Length/1MB ) -gt 2 ) { $count++}; Copy-Item $\_ –Destination $newPath; }
```

Assuming we have 2 files over 2MB in size with the extension txt, we will copy all txt files, and when we check the $count variable, it will equal 2. Now, let's try and shorten this a bit… changing Copy-Item to simply Copy, and using the %

```PowerShell
 GCI | ?{$\_.Name –like "\*.txt"} | %{ if ( ($\_.Length/1MB ) -gt 2 ) { $count++}; copy $\_ –Destination $newPath; }
 ```

 Granted… this only saved us 12 characters… but % is so much cooler than ForEach-Object… it is hard not to use it now.

### Keyboard Shortcuts for Command History

Last I wanted to point out some nice command history manipulation techniques that are useful The MS technet on this is quite good, so I advise checking it out. ([https://technet.microsoft.com/en-us/library/ee176868.aspx](https://technet.microsoft.com/en-us/library/ee176868.aspx)) Particularly interesting is the F7 command, and as useful is the F8 command F7 allows you to simply rerun a previous history item of your choice. F8 allows you to do something simpler to the TAB completion, but using history as the completion. Try typing "GCI \| ?" then hit F8… it will look through your history at any command entered that starts with "GCI \| ?" and cycle through till you find the one you like. F2 is interesting too, but I never remember to use it… but maybe you'd like that too. Enjoy!

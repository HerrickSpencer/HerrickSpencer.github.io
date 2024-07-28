---
layout: post
title: Fun with CoPilot (ChatGPT) in Pull Requests
categories:
- Programming
tags:
- AI
- LM
- ChatGpt
- CoPilot
- Git
- Pull Requests
date: 2024-07-28 19:08 -0700
image: /assets/img/postMedia/ChatGPT/CopilotPRFun.png
---
_*Note*: This post was written back on 2023-09-28 when I was working on a new AI feature, and we were moving super fast. We since have returned to much more rigorous PR policies_

At my work (as with many other programming jobs…) When you submit code changes you have to fill out a description with a template that includes:

* Why this change is needed?
* What was changed?
* How was it tested?

On the last question…. since we have been going at break next speed… there has been NO real testing done. So.. everyone is answering "Manually tested" in that area.

However… I got bored of this and got creative (with a little AI help)  
My latest PRs contained this for "How was it tested?"

> With fingers deft and keen,  
> I tried each feature and routine,  
> By hand and eye, I did make sure,  
> No flaw remained obscure.
>
> Each button and each command,  
> Examined in detail grand,  
> To ensure the software passed,  
> My testing scrutiny, steadfast.
>
> Thus, with methodical delight,  
> I manually tested through the night,  
> And in the morning's light I knew,  
> The program was ready, through and through.
>
> _Emily 'ChatGPT' Dickenson_

Another, when feeling sort of moody:

> "By the power of my mortal hands, I did ascertain its worth."
>
> _Edgar AI-len Poe_

A more apt robotic version:

> I personally executed a thorough examination devoid of any automation to assess the functionality of this particular feature firsthand.

## Prior to any LM

> By pixies.

> By using many of the tests asked for by design/PM…. Then wingin' it.

> not very well.

> While eating Lunch.

> Using the manual test cases designed in the development spec for this feature... and a dowsing rod.

## ChatGPT editions with some added flair

> "By the thunderbolts of Olympus, I have personally put it to the test!" - Zeus

> TIL: "Manually tested" in the warlike tongue of Klingons would be expressed as "Qapla' yIbpu'!" which literally translates to "Let's manually test it with success!" As for how a Klingon would scream it in battle, it might sound something like "QAPLA' YIBPU'!" with a fierce growl and a swing of their weapon to strike their opponent.

> In the clandestine language of the digital underworld, “not applicable” morphs into the enigmatic cipher: “n0t 4pp1c4bl3”.


This one the line was real... but I had to add a Dall-E image
> I forced the failure to make sure we treated the displays as SDR even on an HDR display.
> ![](/assets/img/postMedia/ChatGPT/PRBugsmash.png){: width="300"}_Then I just put in this generated image_

## Poetic versions

> Manually:
"By hand, I verified the settings’ state,
Ensuring views default to ‘not displayed,’
And values, as anticipated, operate."

> By hand and keen eye,
Checks performed with patient care,
Mano a mano testing.

This one I attempted to do it straight... then went rogue.
>By adding an assert in the code for checking this value in the VideoFrameGenerator when on a HDR monitor.
>Also testing on a monitor that is SDR to see if that assert pops correctly.
>
>In poetic format:  
>When coding on a HDR monitor  
>I add an assert to check the val-o  
>Of the VideoFrameGenerator  
>That will report SDR as mal-o.  
>
>But what if I switch to SDR  
>Will the assert still pop as expected?  
>Or will it cause an error  
>And make the code rejected?  


Please use your ChatGPT/CoPilot powers for good... not for evil like I have.

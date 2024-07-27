---
layout: WPArchive
title: Under Siege in a Trojan (Virus) War!
date: 2010-01-28 15:06
author: herrickspencer
comments: true
categories: [Technology]
tags: [Malware Defense, virus, trojan, worm]
---
Last weekend, a virus got through all my defenses… ironic considering where I work (for a MS team that works on server security). My home PC was under siege for about 24hrs, after \[someone\] clicked on a fake window proclaiming to have found an infection in the system, and offering to fix it. .. Please people… don’t click these pop-ups. Don’t use the ‘click-it to make it go away’ approach to computing! Read the messages, evaluate the source for authenticity, and take a prudent approach (even paranoia works) to allowing programs/web pages to run processes on your system.

The first assault in this case was a web based popup alerting the user there was a virus detected, and asking if they would like to install [“Malware Defense”](http://trojan-killer.net/tag/malware-defense/) a fake anti-virus program that actually is a Trojan horse that creates a worm on the system to assist other viruses in their efforts to munch away at your system.

#### Symptoms/Solutions:

|     |     |
| --- | --- |
| **Symptom found** | **Attempted Solution/remedy** |
| The first evidence I saw that the system was infected, since I arrived after the initial infection, was pop-up alerts in the system tray telling me “a malware infection in foo-bar.exe has been detected, do you want this item cleaned?” When you click yes, you are actually allowing a new process to startup and further infect the system. | Don’t click on these, or simply close the window without choosing an option. |
| If you start task manager \[ctrl-shift-esc\] you will find extra suspicious processes running | · “mdefense.exe” in the process list… kill this.<br><br>· You may see more “iExplorer.exe” processes than you actually have running… best to kill these too, MD seems to attach itself to all internet browsers, BTW – Firefox was the one being used at the time of infection, and is one that MD attacks.<br><br>· You may see processes running names like “install…” if you aren’t doing updates or installs… kill these too. |
| By going to the temp directory for the current user, type “\%temp\%” into Windows Explorer, you will find several exe’s and dll’s that are actually viruses, and one of which is a file named “\$startup\$” believed to be used to assist in starting the program on reboots. | Before rebooting, make sure all files are deleted from this folder. Use [Process Explorer](http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx) to locate processes holding on to your files and kill them if necessary |
| Also you will find several changes to your registry that contain references to either “Malware Defense” or “mdefense.exe”. These are ALL over the place. Obviously you’ll find them in the normal startup locations, but they exist in other places as well since MD pretends to be a real program. | DO THIS WITH CARE!! Expert advice recommended:<br><br>Use the search \[ctrl-F\] and search for “Malware Defense” and “mdefense”. Delete keys, careful to leave items that are valid |
| MD seems to use Java quite extensively. | By removing the JRE installs you can greatly reduce its power. Make sure you get all JRE and updates. |
| MD will kill any Antivirus program you try to start or install. It seems to have a quite large list of AV applications that it will block. However, it doesn’t seem that smart about how it blocks them, and only checks the install name or process name of the program. | This is an easy fix (for some AV’s). Simply change the name of the install to get it to install. In some cases this is enough, others you will need to change the name of the starting process for that AV prior to running it. |
| Hijacked Browsers – sites are redirected to ones MD wants you to go to. These include Microsoft.com and most AV sites. | Use task manager to kill all Java running like “jushed” and “java”. Check for other processes that start with J (look at their names before just killing like a mad-man)<br><br>After this, sites seem to route correctly (for a while) |
| Task Manager/System Restore/Safe Mode disabled | Geezeee.. This didn’t happen to me, but you might need to use alternate methods like [Process Explorer](http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx) or boot from an on the disc OS to edit the files… good luck! |
| Services Disabled or not starting. This included Security Center (used for AV and Firewall) and ICS (internet connection sharing) | To fix this you will need to edit the properties of these services, change them from Disabled to Automatic. If this does not work it has been disabled via a registry entry, and you will need to revert this. |
| “Commercial” keeps playing through the speakers. All sorts, car commercials, medical items.. etc. | This is run through an iExplorer process. Find it and kill it in task manager. |

Whatever happens, work on killing java, and get an AV process started cleaning your system. If all else fails you will need to reinstall or revert your system OS.. This, in the end, is what I decided to do. We were able to get the machine back to a useable state for some time, but ultimately, there were still symptoms that the machine was still compromised, and I didn’t want to trust it. Luckily, I’d partitioned my machine up in such a way that this is much easier to do. All my personal files are kept on a separate partition, and in some cases drive, than the OS. This makes the process much less painful, since you don’t worry about losing files.

I’ll give more detail in my next blog entry about this, and my experience trying Virtual PC (to limit any future malware attacks in the future.)
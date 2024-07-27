---
layout: WPArchive
title: A Virtual Adventure in PC protection
date: 2010-02-01 11:08
author: herrickspencer
comments: true
categories: [Technology]
tags: [Virtual PC, virus]
---
![VirtPC](https://www.techwarelabs.com/articles/editorials/virtual_double/images/virtual.jpg)

In my last [post on fighting off a trojan horse virus,](https://herrickspencer.spaces.live.com/Blog/cns!DB2DE5E67B922610!309.entry) I mentioned that I decided to protect my newly installed OS by attempting a foray into the world of virtual machines.  My reasons for doing this are really simple, if I work exclusively in a virtual machine running on the host, it is less likely that an infection will dig down to the host machine and infect the main physical OS.  Virtual machines run on the host via two simple files. One represents the machine and all its settings, while the other represents the virtual hard drive for that machine. To back up this machine, all you have to do is backup those two files.  My strategy was to simply create the host machine, install Virtual PC, and then create the virtual machine. Then I’d be able to backup the VM’s two files, and if I ever was infected again, I’d simply stop that VM, delete it’s files, and copy over the backed up files, restart the machine and I’m back in business. No sweat. (that is my current theory at least)

For more info about what a virtual machine is.. [check this out](https://en.wikipedia.org/wiki/Virtual_machine), but essentially, it is a software representation of a real machine. It is a machine that runs virtualized on a physical machine, using abstractions to access the hardware of the host. Currently Windows7 contains tons of [virtualization](https://www.microsoft.com/windows/virtual-pc/) that emulates previous versions of Windows to run legacy software. [Virtual PC 2007](https://www.microsoft.com/windows/virtual-pc/support/virtual-pc-2007.aspx) is the previous version of this for use in XP and Windows Server to create VM’s

![NA](https://downloads.phpnuke.org/screenshots/33858/300x275x19114c578d.jpg)

## Picking a Virtual Machine product

After comparing the two top contenders in this field [VMWare](https://www.vmware.com/) and [Microsoft Virtual PC](https://www.microsoft.com/windows/virtual-pc/support/virtual-pc-2007.aspx), I opted for the later. There was a couple reasons for this:

1.  Although the VMWare solution was said to have better performance and had more features than Virtual PC, most of the blog entries comparing the two were years old, and were no longer accurate. For example, VMWare was said to support USB sharing, while VPC was not. This is no longer true. In the latest release this feature is included in the MS offering. 
2.  The cost of VMWare was high for someone like me who is using for personal use, and experimentation at that. (I think they might offer a free beta)  Windows Virtual PC is a free offer.
3.  I am trying to be a ‘company man’ and test out the offerings of my own company.  I’ve tried VMWare at another company, though this was an older version of such.

## First stage was to setup the host:

1.  Installed XP Pro
2.  Cleaned up all other partitions (moved old files to a large file server to free up some space for the VM)
3.  Did all windows updates… this took a while moving from XP Pro, adding all service packs etc. 
    1.  remember to check for updates multiple times, as one set of updates will usually require a reboot. Going back to the update site till no more critical updates exist will bring this machine totally up to snuff.
4.  Added [Microsoft Security Essentials](https://www.microsoft.com/security_essentials/) to cover the anti-malware solution on this machine.
5.  Installed [Virtual PC 2007](https://www.microsoft.com/windows/virtual-pc/support/virtual-pc-2007.aspx)

## Next stage: Create a VM (virtual machine)

1.  Created a new VM (virtual machine) and made sure to deploy it onto a **separate drive from the OS,** this is important. Reason being, your biggest performance waster is IO (Input Output) of information to the hard drive.  If you put the VM files on the same disk as the OS, they will be fighting to share the drive head to retrieve and write data. Make it nice for your new VM and put these files on a different hard drive (make sure it’s not just a partition on the same drive!).
2.  Only gave it half of my host’s memory, this was only a personal choice. I noticed that the VM was using lots of CPU, but not much memory, so I didn’t allow it to starve the host OS by limiting the VM to only a portion of the total.

## Get the VM up to speed

Last but not least, had to get the VM up and running. This step is very similar to setting up the host (save adding Virtual PC).

1.  Installed XP Pro
2.  Did all windows updates… (again …long time; remember to get all updates as done in host)
3.  Added [Microsoft Security Essentials](https://www.microsoft.com/security_essentials/) to cover the anti-malware solution on this machine.
4.  Added my favorite software ([Xplorer2](https://www.zabkat.com/), [VLC](https://www.videolan.org/vlc/), [UltraEdit](https://www.ultraedit.com/)…) but only ones that I know are safe and contain no threats.
5.  Shutdown the VM, and backed up the VMH files (should be 2)  I backed these up to a completely different machine JIC
6.  Restarted the VM and installed all the unsafe software.. (you know you have some)

## Final thoughts

Now I’m back in business!  Seems to be working great, don’t even notice that I”m not on a ‘real’ machine most of the time.  I’ll update this blog if I see any issues that are presented by using this method.  So far I’ve only seen one tiny issue.

I use this machine exclusively for watching TV and movies via [Hulu](https://www.hulu.com/) and my own video library.  One issue that seems odd, is that if you put the VM into full-screen mode, then use the full-screen mode in Hulu, the video will freeze, although the audio keeps playing.   I’m still looking for a solution to this problem, and will post that as well if I find one.

Another interesting note, if you work from home, and your company has restrictions on Instant messaging, or what you can surf to, while using thier VPN, you could use this method to do that also. Simply launch the VM and use that for your companies VPN, and use the host for your own personal work. This way they will have no way of tracking the traffic you do on the host.  I know someone who is doing this… I’ll see if I can get an update for that as well.
